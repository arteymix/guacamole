Guacamole
=========
Guacamole is a plateformer, side-scroller and networked game based on socket.io
and MongoJS.

It is designed to minimize the server communication and let client share their
states over WebSocket.

Gettings started
----------------
To start playing in a very few steps:

1. clone the project or just download a zipped release on GitHub ;
2. start the server with `python guacamole/app.py` ;
3. open your browser at `http://127.0.0.1:5000` ;
4. open your firewall on port 5000 and share your local ip to your friends.

Report any bugs or request on [GitHub issues]().

Client
--------
The frontend is the coolest part.

Server
-------
The server is written in Python using Flask micro-framework. It manages rooms,
generate the map in the TMX format and distribute the client code.

