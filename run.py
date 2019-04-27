from sanic.log import logger
from dotenv import load_dotenv, find_dotenv

from Tx.Tx import app
from Tx.util import sanic_config_manager
from utils import env_bool, env_int, env_str

DEBUG = env_bool("SANIC_DEBUG", True)
if DEBUG:
    load_dotenv(find_dotenv())

sanic_config_manager(app, prefix="SANIC_")


if __name__ == "__main__":

    app.run(host="0.0.0.0", port="8000", workers=1, debug=DEBUG)
