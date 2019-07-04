import os

from raven.response.abstract_response import BaseResponse

from raven.utils import template_name_from_class_name


class GetListOfTask(BaseResponse):
    """
    This is a implement from `name` in intent name.
    """

    def __init__(self, scope=None):
        super(GetListOfTask, self).__init__(self, scope)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(GetListOfTask, self).render(class_name=self.class_name, sub_path="_task")

        return self.render_template.render(return_text=list("abn"), pretty=pretty)
