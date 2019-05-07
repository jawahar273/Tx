from Bot.Bot_response.abstract_response import BaseResponse

from Bot.Bot_response.utils import geneate_response_from_intent


class Greeting(BaseResponse):
    def __init__(self, scope=None):

        super(Greeting, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Greeting, self).render(class_name=self.class_name, sub_path="_global")

        temp = geneate_response_from_intent(
            "greeting_response.yml", "_greeting", "_global"
        )

        return self.render_template.render(pretty=pretty, response_text=temp)
