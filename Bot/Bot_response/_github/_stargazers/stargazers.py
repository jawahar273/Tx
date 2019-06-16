from Bot.Bot_response.abstract_response import BaseResponse


class Stargazers(BaseResponse):

    def __init__(self, scope=None):

        super(Stargazers, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Stargazers, self).render(
            class_name=self.class_name, sub_path='_github'
        )

        return self.render_template.render(pretty=pretty)