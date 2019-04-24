import os

from TxBot_response.abstract_response import TxAbstractResponse

from utils import template_name_from_class_name


class GetListOfTask(TxAbstractResponse):
    '''
    This is a implement from `name` in intent name.
    '''

    def __init__(self):
        super(GetListOfTask, self).__init__(self)

    def render(self):

        class_name = self.__class__.__name__  # class name
        template = None

        template = os.path.join(os.path.dirname(__file__),
                                template_name_from_class_name(class_name)
                                )

        with open(template) as _template_file:

            template = self.template(
                _template_file.read()
            )

        return template.render(return_text=[])
