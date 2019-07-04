from raven.response.abstract_response import BaseResponse


class Projects(BaseResponse):
    def __init__(self, scope=None):

        super(Projects, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Projects, self).render(class_name=self.class_name, sub_path="_profile")

        return self.render_template.render(pretty=pretty)
