from server.main import app, socketio
from config.stage import settings

if __name__ == "__main__":
    socketio.run(app, debug=settings.DEBUG)
