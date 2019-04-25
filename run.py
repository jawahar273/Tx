from os import getenv
from sanic.log import logger
from dotenv import load_dotenv, find_dotenv

from Tx.Tx import app
from Tx.util import sanic_config_manager

load_dotenv(find_dotenv())

sanic_config_manager(app, prefix="SANIC_")


if __name__ == "__main__":

    logger.info(f'running the server {getenv("SANIC_POSTGRES_PORT")}')
    app.run(
        host="0.0.0.0",
        port="8000",
        debug=getenv('DEBUG', True),
    )
