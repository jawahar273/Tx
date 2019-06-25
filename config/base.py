from os import getenv

from dotenv import load_dotenv

from jinja2 import Environment, FileSystemLoader, select_autoescape

from utils import import_class

# loading the env variables
load_dotenv()

# Template settings

render_template = Environment(
    loader=FileSystemLoader(["templates", "Bot/Bot_response/templates"]),
    autoescape=select_autoescape(["html", "xml"]),
)

# NLU Engine settings
engine_param = {
    "dataset_path": "Bot/storage/_profile/dataset/dataset.json",
    "next_class": "Bot.Bot_input.rest_input.RESTInput",
    "input_params": {},
    "output_params": {},
    "is_next": False,
}

# logger settings
logger = import_class("logging.Logger")

# Validation REGEX

# Standard RFC 5322, url: https://emailregex.com/
EMAIL_VALID_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

# Intent and Dataset storage
DEFAULT_STARTPOINT = "Bot.storage"

