from importlib import import_module as imm
from os import getenv
from datetime import datetime 

# from config.stage import heartbeat_meta


def render_template_file(file_name: str, **kwargs: dict):
    """
    Higher level api for rendering templates.
    """
    from config.stage import settings

    return settings.render_template.get_template(file_name).render(**kwargs)


def import_module(path):

    if isinstance(path, str):

        return imm(path)

    else:

        raise TypeError("Wrong data type give, parameter must of path in str()")


def import_class(path):

    if isinstance(path, str):

        value, class_name = path.rsplit(".", 1)

        module = import_module(value)
        return getattr(module, class_name)

    else:

        raise TypeError("Wrong data type give, parameter must of path in str()")


def env_str(env_name: str, default: str) -> str:

    return getenv(env_name, default)


def env_int(env_name: str, default: int) -> int:

    return int(getenv(env_name, default))


def env_float(env_name: str, default: float) -> float:

    return float(getenv(env_name, default))


def env_bool(env_name: str, default: bool) -> bool:

    return bool(getenv(env_name, default))

# def is_alive_scheduler():
#     '''
#     Check the schedular is alive and running with set of interval of loop.
#     '''
#     if heartbeat_meta:
        
#         diff = heartbeat_meta['last_checkpoint'] - datetime.now()
#         if diff >= 6:
#             return False
#         return True
    
#     else:
#         return False