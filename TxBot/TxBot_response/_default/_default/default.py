from TxBot.TxBot_response.abstract_response import TxBaseResponse


class Default(TxBaseResponse):
    def __init__(self):
        super(Default, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Default, self).render(class_name=self.class_name, sub_path="_default")

        return self.render_template.render(pretty=pretty)
