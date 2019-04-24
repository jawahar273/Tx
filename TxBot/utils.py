from importlib import import_module
from re import split

from config import CMD_SYMBOLE_STOP, CMD_SYMBOLE_START, TEMPLATE_FORMATE


def import_class(path):

    value, class_name = path.rsplit(".", 1)
    module = import_module(value)
    return getattr(module, class_name)


def parse_cmd(cmd, stop_symbol):
    """
    Parse the given cmd value with the symbol in
    config.CMD_SYMBOLE
    """
    if stop_symbol:
        return f"{CMD_SYMBOLE_START}{cmd}{CMD_SYMBOLE_STOP}"

    return f"{CMD_SYMBOLE_START}{cmd}"


def parse_cmd_value(value):

    patten = CMD_SYMBOLE_START + r"\w+" + CMD_SYMBOLE_STOP
    return split(patten, value)[1].strip()


def template_name_from_class_name(value):
    '''
    Template name return for the template.
    '''
    return invert_title(f'{value}.{TEMPLATE_FORMATE}')


def invert_title(value):

    return value[0].lower() + value[1:]