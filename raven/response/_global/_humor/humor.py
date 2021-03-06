"""

Humor
-----

Bot are need to more friendly ah. Some-time we might me low on energy we
might need joke to boost our self. This response return with some level
of humber to user.

For example:

.. code-block:: yaml

    - tell me some jokes
    - Do know any jokes
    - I am sad today

"""
import os
from random import randint

import yaml

from raven.response.abstract_response import BaseResponse


class Humor(BaseResponse):
    def __init__(self, scope=None):

        super(Humor, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Humor, self).render(class_name=self.class_name, sub_path="_global")

        return self.render_template.render(
            pretty=pretty, response_text=self.get_humor_response()
        )

    def get_humor_response(self):
        """
        Deperate in favour of `raven.response.utils.geneate`_response_from_intent
        Select random humor from the give file.
        """
        # need better alternative
        humor_response_path = os.path.join(
            "raven", "response", "_global", "_humor", "humor_response.yml"
        )
        with open(humor_response_path) as _response:

            try:

                _response = yaml.safe_load(_response)
                total_temp = len(_response["responseText"]) - 1
                # selecting random humor sentence
                _response = _response["responseText"][randint(0, total_temp)]

            except yaml.YAMLError as e:

                _response = "Error in returning humor response"

            return _response
