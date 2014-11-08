from flask import Flask, render_template
from flask.ext.socketio import SocketIO, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def guacamole():
    return render_template('guacamole.html')

@socketio.on('connect')
def connect():
    exit(1)
    app.logger.info('we got a logger!')
    print('we got a logger!')
    pass

@socketio.on('message')
def message(message):
    print('we got a message', message)
    app.logger.error('we got a message')
    app.logger.info('we got a logger! {}'.format(message))

@socketio.on('disconnect')
def disconnect():
    pass

@socketio.on('json')
def json(json):
    print('received json: ' + str(json))

@socketio.on('join')
def join(data):
    join_room(data['room'])
    print('{} has joined the room {}'.format(data, data['room']))

@socketio.on('leave')
def join(data):
    leave_room(data['room'])
    print('{} has left the room {}'.format(data, data['room']))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
