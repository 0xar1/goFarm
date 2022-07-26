from socket import SocketIO
from time import sleep
from flask import Blueprint,redirect, request,url_for, render_template,flash
from flask_login import login_required,current_user
from ..models import *
from .. import socketio
# from ..webapp import socketio
from flask import current_app as app
from flask_socketio import emit,send
from ..forms import SellForm


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

    return render_template('auction.html',aucid = id)

# for testing 
@auctions.route('/auction')
@login_required
def auctionold():
    
    return render_template('auctionold.html')

# @auction.route('/auctionnotfound')
@socketio.on('message')
def message(data):
    print(f"\n\n{data}\n\n")
    send(data)
    seconds = 5
    for i in range(seconds):
        send(seconds)
        seconds -= 1
        sleep(1)
    
@auctions.route('/buy')
@login_required
def buy():
    d = Auction.query.all()
    return render_template('buy.html',title="Upcoming Auctions - goFarm",data = d )

@auctions.route('/live')
@login_required
def live():
    d = CurrentAuction.query.all()
    return render_template('currentAuctions.html',title="Live Auctions - goFarm",data = d )

@auctions.route('/sell', methods=['GET','POST'])
@login_required
def sell():
    form = SellForm()
    # print('\n\n\n')
    # print(current_user.__dict__)
    # print('\n\n\n')
    if form.validate_on_submit():
        crop_name = form.cropname.data.name
        crop_variety = form.variety.data
        crop_minPrice = form.minprice.data
        crop_dateTime = form.datetime.data
        auction_exist = Auction.query.filter_by(datetime = crop_dateTime).first()
        if auction_exist is None:
            data = Auction(
                sellerId = current_user.uid,
                sellerName = current_user.full_name,
                cropName = crop_name,
                # cropId  = take from Session 
                variety = crop_variety,
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