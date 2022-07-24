from socket import SocketIO
from time import sleep
from flask import Blueprint,redirect,url_for, render_template,flash
from flask_login import login_required,current_user
from ..models import *
from .. import socketio
# from ..webapp import socketio
from flask import current_app as app
from flask_socketio import emit,send


auctions = Blueprint('auctions', __name__,template_folder='auctionTemplate')

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)

@auctions.route('/auction')
@login_required
def auction():
    return render_template('auction.html',title="Auction - goFarm")


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
    return render_template('buy.html',title="Buy - goFarm",data = Crops.query.all() )

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