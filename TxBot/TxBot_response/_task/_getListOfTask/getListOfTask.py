import os

from TxBot_response.abstract_response import TxBaseResponse

from utils import template_name_from_class_name


class GetListOfTask(TxBaseResponse):
    '''
    This is a implement from `name` in intent name.
    '''

    def __init__(self):
        super(GetListOfTask, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self):

        self.class_name = self.get_class_name()  # class name

        super(GetListOfTask, self).render(class_name=self.class_name, sub_path='_task')

        return self.render_template.render(return_text=list('abn'))
