from abc import ABC, abstractmethod
import os

from jinja2 import Template

from config import IGNORABLE_THESHOLD_VALUE
from utils import template_name_from_class_name, invert_title_case as _title

# class TxAbstractResponse(ABC):


class TxAbstractResponse(ABC):
    '''
    Name of the sub class must be matching to
    the intent with title-case such as.

    .. code:: python
        type: intent
        name: getList
        $class: getList
        ...

    '''

    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError('__init__ must be implemented')

    @abstractmethod
    def render(self, *args, **kwargs):
        raise NotImplementedError('Response is not implemented')

    @abstractmethod
    def get_class_name(self):
        raise NotImplementedError('get_class_name must be implemented')

    @abstractmethod
    def check_intent_name(self, *args, **kwargs):
        raise NotImplementedError('check_intent_name must be implemented')


class TxBaseResponse(TxAbstractResponse):

    def __init__(self, *args, **kwargs):
        self.template = Template
        # to reject if the probility of intent is less than
        # theshold value.
        self.theshold_value = IGNORABLE_THESHOLD_VALUE
        self.default_response = '''I am unable to understanding what you asked. Could you repeate what you have said. If you are using shorthand use without mistake'''

    def render(self, *args, **kwargs):
        # raise NotImplementedError('Response is not implemented')
        self.class_name = kwargs.get('class_name')

        self.render_template = os.path.join(os.path.dirname(__file__),
                                            kwargs.get('sub_path'),
                                            f'_{_title(self.class_name)}',
                                            template_name_from_class_name(
                                                self.class_name)
                                            )

        with open(self.render_template) as _template_file:

            self.render_template = self.template(
                _template_file.read()
            )


    def get_class_name(self):
        raise NotImplementedError('get_class_name must be implemented')

    def check_intent_name(self, name):
        return name.startswith(f'{self.get_class_name()}Intent')
