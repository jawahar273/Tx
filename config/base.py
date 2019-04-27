from jinja2 import Environment, FileSystemLoader, select_autoescape
from utils import import_class

# Template settings

render_template = Environment(
    loader=FileSystemLoader(["Tx/templates", "TxBot/TxBot_response/"]),
    autoescape=select_autoescape(["html", "xml"]),
)


# NLU Engine settings
engine_param = {
    "dataset_path": "TxBot/storage/_profile/dataset/dataset.json",
    "next_class": "TxBot.TxBot_input.rest_input.RESTInput",
    "input_params": {},
    "is_next": False,
}


# logger seetings
logger = import_class("sanic.log.logger")
