from TxBot.TxBot_response.abstract_response import TxBaseResponse


class Projects(TxBaseResponse):
    def __init__(self):

        super(Projects, self).__init__(self)

    def get_class_name(self):

        return self.__class__.__name__

    def render(self, pretty=None):

        self.class_name = self.get_class_name()  # class name

        super(Projects, self).render(class_name=self.class_name, sub_path="_profile")

        return self.render_template.render(pretty=pretty)
