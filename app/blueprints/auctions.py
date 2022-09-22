import json
from socket import SocketIO
from time import sleep
from flask import Blueprint,redirect, request,url_for, render_template,flash,request
from flask_login import login_required,current_user
from ..models import *
from .. import socketio
# from ..webapp import socketio
from flask import current_app as app
from flask_socketio import emit,send
from ..forms import SellForm
from datetime import datetime, timedelta


auctions = Blueprint('auctions', __name__,template_folder='auctionTemplate')

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)

@auctions.route('/auction/<id>')
@login_required
def auction(id):
    temp = CurrentAuction.query.filter_by(aid=id).first()
    if temp is None:
        return render_template('notfound.html')
    return render_template('auction.html',aucid = id,data = temp)


# new auction here 
@auctions.route('/trade/<tradeid>')
@login_required
def trade(tradeid):
    tempData = tempTable.query.filter(tempTable.aid == tradeid).order_by(tempTable.userBid.desc()).limit(10).all()
    temp = CurrentAuction.query.filter_by(aid=tradeid).first()
    k = db.session.query(CurrentAuction.datetime).filter(CurrentAuction.aid == tradeid).first()
    
    # print("\n\n",tempData[1],"\n\n")
    if tempData:
        minPrice = tempData[0].userBid
        winner = tempData[0].buyerName
        a = k.datetime
        time = a + timedelta(hours=1)
    else:
        minPrice = ""
        winner = ""
        time = ""
    if temp is None:
        return render_template('notfound.html')
    return render_template('new_auctions.html', tableData = tempData,time = time,auctiondata = temp,minPrice = minPrice,winner = winner)



# for testing 
# @auctions.route('/auction')
# @login_required
# def auctionold():
    
#     return render_template('auctionold.html')


# @socketio.on('message')
# def message(data):
#     print(f"\n\n{data}\n\n")
#     send(data)
    # seconds = 5
    # for i in range(seconds):
    #     send(seconds)
    #     seconds -= 1
    #     sleep(1)

@socketio.on('bidData')
def bidvalue(data):
    id = data['id']
    userBid = data['userBid']
    minRate = data['minRate']
    print("\n\n",id,":",userBid,"\n\n")
    inserData = tempTable(aid=id,userBid = userBid, buyerid = current_user.uid,buyerName = current_user.full_name)
    db.session.add(inserData)
    db.session.commit()
    temp = []
    fetchData = tempTable.query.filter_by(aid = id).order_by(tempTable.userBid.desc()).limit(10).all()
    for i in fetchData:
        temp.append(i.buyerName)
        temp.append(i.userBid)
    emit('reloadTable',temp,broadcast=True)

@socketio.on('reloadData')
def reload(data):
    id = data
    temp = []
    fetchData = tempTable.query.filter_by(aid = id).order_by(tempTable.userBid.desc()).limit(10).all()
    for i in fetchData:
        temp.append(i.buyerName)
        temp.append(i.userBid)
    emit('reloadTable',temp,broadcast = True)

@socketio.on('table')
def initial(data):
    a = tempTable.query.filter_by(aid = data).order_by(tempTable.userBid.desc()).limit(10).all()
    x = []
    for i in a:
        x.append(i.buyerName)
        x.append(i.userBid)
    print(x)
    emit('get_table_data',x,broadcast = True)

@socketio.on('submitbid')
def submitbid(data,id):
    dbval = tempTable(aid=id,userBid = data,buyerid = current_user.uid,buyerName = current_user.full_name)
    db.session.add(dbval)
    db.session.commit()
    emit('table',id)

@auctions.route('/buy')
@login_required
def buy():
    # d = Auction.query.all()
    d = db.session.query(Auction,Crops,User).filter(Auction.sellerId == User.uid).filter(Auction.cropId == Crops.cropId).all()
    return render_template('buy.html',title="Upcoming Auctions - goFarm",data = d )

@auctions.route('/live')
@login_required
def live():
    # d = CurrentAuction.query.all()
    d = db.session.query(CurrentAuction,Crops,User).filter(CurrentAuction.sellerId == User.uid).filter(CurrentAuction.cropId == Crops.cropId).all()

    return render_template('currentAuctions.html',title="Live Auctions - goFarm",data = d )

@auctions.route('/sell', methods=['GET','POST'])
@login_required
def sell():
    form = SellForm()
    temp = []
    k = db.session.query(Crops.name).distinct(Crops.name).all()
    for i in range(0,len(k)):
        print(k[i].name)
        a = k[i].name
        temp.append(a)

    form.cropname.choices = temp

    # print('\n\n\n')
    # print(current_user.__dict__)
    # print('\n\n\n')
    if form.validate_on_submit():
        crop_name = form.cropname.data
        crop_variety = form.variety.data
        crop_amount = form.amount.data
        crop_minPrice = form.minprice.data
        crop_dateTime = form.datetime.data
        cropId = db.session.query(Crops.cropId).filter(Crops.name == crop_name).filter(Crops.variety == crop_variety).first()
        auction_exist = Auction.query.filter_by(datetime = crop_dateTime).first()
        if auction_exist is None:
            data = Auction(
                sellerId = current_user.uid,
                # sellerName = current_user.full_name,
                # cropName = crop_name,
                # cropId  = take from Session 
                cropId = cropId[0],
                variety = crop_variety,
                amount = crop_amount,
                minPrice = crop_minPrice,
                datetime = crop_dateTime
            )
            db.session.add(data)
            db.session.commit()
            return redirect(url_for('dashboard'))
        print('\n\n')
        flash('')
    return render_template('sell.html',form = form,title="Sell - goFarm")

# @socketio.on('message')
# def message(data):
#     print(f"\n\n{data}\n\n")
#     send(data)
#     seconds = 20
#     for i in range(seconds):
#         send(data)
#         seconds -= 1
#         sleep(1)
#     print(current_user.uid)

@auctions.route('/ledger')
@login_required
def ledger():
    d = Auction.query.all()

    c = tempTable.query.all()
    return render_template('ledger.html',title="Auction History - goFarm",auction = d,temp = c )
