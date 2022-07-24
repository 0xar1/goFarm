# from app import app,db,socketio
# from app.models import *
from app import create_app, socketio

app = create_app(debug=True)

if __name__ == '__main__':
    socketio.run(app,debug=True,host = '0.0.0.0')



