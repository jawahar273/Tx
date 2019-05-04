from Bot.Bot_response.abstract_response import BaseResponse


class Humor(BaseResponse):
    def __init__(self, scope=None):

        super(Humor, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Humor, self).render(class_name=self.class_name, sub_path="_global")

        return self.render_template.render(pretty=pretty)
