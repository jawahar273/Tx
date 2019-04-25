from importlib import import_module
from re import split, search

from config import CMD_SYMBOLE_STOP, CMD_SYMBOLE_START, TEMPLATE_FORMATE



def _title_case(value):
    '''
    Return the title of the string but the
    first letter is affected.
    '''
    return value[0].upper() + value[1:]


def invert_title_case(value):
    '''
    Invert the title case in a string which
    it do only lower the case of the first letter
    and return all the same.
    '''
    return value[0].lower() + value[1:]


def import_class(path):

    value, class_name = path.rsplit(".", 1)
    module = import_module(value)
    return getattr(module, class_name)


def import_response_intent(intent_name):
    '''
    @params intent_name intent name from yaml
    @params sub_path place with intent fiels and respose folders
     such as `_profile`.
    '''

    temp = intent_name.split('Intent')
    intent_name = temp[0]
    sub_path = temp[1]
    path = f'TxBot_response.{sub_path}._{intent_name}'
    path = f'{path}.{intent_name}.{_title_case(intent_name)}'
    try:
        return import_class(path)
    except ModuleNotFoundError:
        path = f'TxBot.{path}'
        return import_class(path)



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
    return invert_title_case(f'{value}.{TEMPLATE_FORMATE}')


def windows_path_regex(path):
    '''
    Find the give path is window path using regular
    expression.
    '''
    regex = r"[a-zA-Z]:\\((?:.*?\\)*).*"
    return True if search(regex, path) else False

