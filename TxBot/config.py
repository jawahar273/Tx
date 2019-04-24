from blinker import signal

# PROCESSED_INPUT = 'PROCESSED_INPUT'
ASSERTTYPE = "ASSERTTYPE"
PROCESSED_INPUT = "process_input"
FOR_OUTPUT = "process_output"

SKIP_OUTPUT = "SKIP_OUTPUT"

# cmd related config
COMMANDS = {"WIKI": {"name": "wiki"}, "EXIT": {"name": "exit"}}
CMD_SYMBOLE_START = ":"
CMD_SYMBOLE_STOP = " "

# To stop run wanted running layer signal will be used.
STOPLAYERNAME = "STOPLAYER"
STOPLAYER = signal(STOPLAYERNAME)

# Template File Formate
TEMPLATE_FORMATE = 'html'