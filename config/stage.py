from os import getenv

from importlib import import_module

settings = import_module(getenv("CONFIG", "config.local"))
logger = settings.logger
db = settings.db