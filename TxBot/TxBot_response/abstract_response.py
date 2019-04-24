from abc import ABC, abstractmethod

from jinja2 import Template


class abstractstatic(staticmethod):
    __slots__ = ()
    def __init__(self, function):
        super(abstractstatic, self).__init__(function)
        function.__isabstractmethod__ = True
    __isabstractmethod__ = True


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
        self.template = Template

    @abstractmethod
    def render(self, *args, **kwargs):
        raise NotImplementedError('Response is not implemented')
