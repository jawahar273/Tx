from Bot.Bot_response.abstract_response import BaseResponse

from Bot.config import FOR_OUTPUT


class Commands(BaseResponse):
    def __init__(self, scope=None):

        super(Commands, self).__init__(self, scope=scope)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, txObject, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Commands, self).render(class_name=self.class_name, sub_path="_command")

        return self.render_template.render(
            output_values=txObject.get(FOR_OUTPUT), pretty=pretty
        )
