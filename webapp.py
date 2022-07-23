# from app import app,db,socketio
# from app.models import *
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app)


# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User,'Crops': Crops,'Auction': Auction}
