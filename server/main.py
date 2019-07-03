from flask import Flask
from flask_socketio import SocketIO, emit

from Bot.Bot_engine.default_engine import DefaultEngine as Engine
from Bot.Bot_input.rest_input import RESTInput
from Bot.Bot_output.rest_output import RESTOutput
from Bot.Bot_layer.cmd.wiki import WikiLayer

from config.stage import settings

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)

reset_input = RESTInput(settings.engine_param)
rest_output = RESTOutput()
engine = Engine(reset_input, rest_output, settings.engine_param)
engine.add([WikiLayer({})])

# reset_input.toBotText(text)


@socketio.on("from_client")
def get_response(data):
    print("........................")
    reset_input.toBotText(data["text"])
    emit("from_server", {"response": engine.go(pretty="json.html")})
