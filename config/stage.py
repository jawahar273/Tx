from os import getenv

from importlib import import_module

setting = import_module(getenv("CONFIG", "config.local"))

logger = setting.logger
