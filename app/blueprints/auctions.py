from flask import Blueprint,redirect,url_for, render_template,flash
from flask_login import login_required
from ..models import *
from flask import current_app as app
from flask_socketio import emit


auctions = Blueprint('auctions', __name__,template_folder='auctionTemplate')

# @socketio.on('message')
# def handle_message(data):
#     print('received message: ' + data)

@auctions.route('/auction')
@login_required
def auction():
    return render_template('auction.html',title="Auction - goFarm")

@auctions.route('/buy')
@login_required
def buy():
    return render_template('buy.html',title="Buy - goFarm")



