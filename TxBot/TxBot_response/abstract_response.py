from abc import ABC, abstractmethod
import os

from config.stage import settings

from TxBot.config import IGNORABLE_THESHOLD_VALUE, TEMPLATE_FORMATE
from TxBot.utils import template_name_from_class_name, invert_title_case, _title_case

# class TxAbstractResponse(ABC):


class TxAbstractResponse(ABC):
    """
    Name of the sub class must be matching to
    the intent with title-case such as.

    .. code:: python
        type: intent
        name: getList
        $class: getList
        ...

    """

    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError("__init__ must be implemented")

    @abstractmethod
    def render(self, *args, **kwargs):
        raise NotImplementedError("Response is not implemented")

    @abstractmethod
    def get_class_name(self):
        raise NotImplementedError("get_class_name must be implemented")

    @abstractmethod
    def check_intent_name(self, *args, **kwargs):
        raise NotImplementedError("check_intent_name must be implemented")


class TxBaseResponse(TxAbstractResponse):
    def __init__(self, *args, **kwargs):
        # to reject if the probility of intent is less than
        # theshold value.
        self.theshold_value = IGNORABLE_THESHOLD_VALUE

    def render(self, *args, **kwargs):

        self.class_name = kwargs.get("class_name")

        # render_template_name = os.path.join(os.path.dirname(__file__),
        #                                     kwargs.get('sub_path'),
        #                                     f'_{_title(self.class_name)}',
        #                                     template_name_from_class_name(
        #                                         self.class_name)
        #                                     )
        render_template_name = (
            f"{invert_title_case(self.class_name)}.{TEMPLATE_FORMATE}"
        )
        render_template_name = (
            f"_{invert_title_case(self.class_name)}/{render_template_name}"
        )
        render_template_name = f'{kwargs.get("sub_path")}/{render_template_name}'

        self.render_template = settings.render_template.get_template(
            render_template_name
        )
        # with open(self.render_template) as _template_file:

        #     self.render_template = self.template(
        #         _template_file.read()
        #     )

    def get_class_name(self):
        raise NotImplementedError("get_class_name must be implemented")

    def check_intent_name(self, name):
        return name.startswith(f"{self.get_class_name()}Intent")
