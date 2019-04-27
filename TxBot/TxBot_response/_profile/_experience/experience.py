from TxBot.TxBot_response.abstract_response import TxBaseResponse


class Experience(TxBaseResponse):
    def __init__(self):
        super(Experience, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    # def render(self, pretty=pretty):
    #     self.class_name = self.get_class_name()  # class name

    #     super(Experience, self).render(
    #         class_name=self.class_name, sub_path="_profile"
    #     )

    #     return self.render_template.render(pretty=pretty)

    def render(self, pretty=None):
        self.class_name = self.get_class_name()  # class name

        super(Experience, self).render(class_name=self.class_name, sub_path="_profile")

        return self.render_template.render(pretty=pretty)
