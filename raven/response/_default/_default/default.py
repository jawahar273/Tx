"""
-------
Default 
-------

Return the default resposne if the user's response is not
understand or out of scope for the bot engine.
"""
from raven.response.abstract_response import BaseResponse


class Default(BaseResponse):
    def __init__(self, scope=None):

        super(Default, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Default, self).render(class_name=self.class_name, sub_path="_default")

        return self.render_template.render(pretty=pretty)
