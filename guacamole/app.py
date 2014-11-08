from flask import Flask, render_template, g
from flask.ext.socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

class Game:
    """A game, simply!"""
    started = False

@app.route('/')
def guacamole():
    return render_template('guacamole.html')

@socketio.on('connect')
def connect():
    app.logger.info('we got a logger!')
    print('we got a logger!')

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
    room = data['room']

    if not room in g.games:
        g.games[room] = Game()

    game = g.games[room]

    join_room(room)

    print('{} has joined the game room {}'.format(data['username'], room))

@socketio.on('leave')
def leave(data):
    room = data['room']

    if not room in g.games:
        return socketio.send('Room {} does not exist.'.format(room))

    leave_room(data['room'])
    print('{username} has left the room {room}'.format(**data))

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
