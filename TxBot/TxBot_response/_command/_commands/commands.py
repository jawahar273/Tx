from TxBot.TxBot_response.abstract_response import TxBaseResponse

from TxBot.config import FOR_OUTPUT


class Commands(TxBaseResponse):

    def __init__(self):

        super(Commands, self).__init__(self)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, txObject):

        self.class_name = self.get_class_name()  # class name

        super(Commands, self).render(
            class_name=self.class_name, sub_path='_command',

        )

        return self.render_template.render(
            output_values=txObject.get(FOR_OUTPUT)
        )