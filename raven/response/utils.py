from os.path import sep, join
from random import randint

import yaml


def geneate_response_from_intent(
    response_file_name: str,
    intent_name: str,
    sub_path: str,
    base_path="raven.response",
    random=True,
) -> str:
    """
    :param response_file_name: file name which content
     the response text which selected based on randomness if true
    """
    response_path = join(
        base_path.replace(".", sep),  # Eg: raven.response
        sub_path,  # Eg: _global
        intent_name,  # Eg: _humor
        response_file_name,  # Eg: humor_response.yml
    )

    with open(response_path) as _response:

        try:

            _response = yaml.safe_load(_response)

            if random:
                total_temp = len(_response["responseText"]) - 1
                # selecting random humor sentence
                _response = _response["responseText"][randint(0, total_temp)]

            else:

                _response = _response["responseText"][0]

        except yaml.YAMLError as e:

            _response = f"Error in returning {intetn_name[1:]} response"

        return _response
