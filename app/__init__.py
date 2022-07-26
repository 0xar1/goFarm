from flask import Flask 
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy #ORM
from flask_migrate import Migrate
from config import Config

socketio = SocketIO()
db = SQLAlchemy()
login = LoginManager()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config.from_object(Config)
    db.init_app(app)
    
    migrate = Migrate(app,db)
    from .blueprints.auth import auth
    from .blueprints.auctions import auctions
    # #flask login
    login.init_app(app)
    login.login_view = 'auth.login'
    socketio.init_app(app)
    with app.app_context():
        from . import routes
        app.register_blueprint(auth)
        app.register_blueprint(auctions)

    from .models import User,Crops,Auction,tempTable,Ledger,CurrentAuction
    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User,'Crops': Crops,'Auction': Auction,'tempTable': tempTable,'Ledger':Ledger,'CurrentAuction':CurrentAuction}
    return app



# app = Flask(__name__)
# #importing the secret key file
# app.config.from_object(Config)

# #SQLAlchemy
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)

# #flask login
# from flask_login import LoginManager
# login = LoginManager(app)
# login.login_view = 'auth.login'

# #importing all routes,models and blueprints
# from app import routes,models
# from app.blueprints.auth import auth 
# app.register_blueprint(auth)

# from app.blueprints.auctions import auctions
# app.register_blueprint(auctions)

# socketio = SocketIO(app)




# app.debug(True)   
