from os import getenv

from blinker import signal

from utils import import_class, import_module, env_str


# PROCESSED_INPUT = 'PROCESSED_INPUT'
ASSERTTYPE = "ASSERTTYPE"
PROCESSED_INPUT = "process_input"
FOR_OUTPUT = "process_output"
NLUSCOPE = "NLUSCOPE"

SKIP_OUTPUT = "SKIP_OUTPUT"

# cmd related config
COMMANDS = {"WIKI": {"name": "wiki"}, "EXIT": {"name": "exit"}}
CMD_SYMBOLE_START = ":"
CMD_SYMBOLE_STOP = " "

# To stop run wanted running layer signal will be used.
STOPLAYERNAME = "STOPLAYER"
STOPLAYER = signal(STOPLAYERNAME)

# Template File Formate
TEMPLATE_FORMATE = env_str("TEMPLATE_FORMATE", "html")

# Response Config
IGNORABLE_THRESHOLD_VALUE = 0.58

# logger Config
logger = None

try:

    # for importing sanic logger
    logger = import_class(getenv("LOGGERCLASS", "sanic.log.logger"))

except (AttributeError, ValueError):

    # importing standard logger module
    logger = import_module(getenv("LOGGERCLASS", "logging"))
