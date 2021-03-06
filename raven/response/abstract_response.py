from abc import ABC, abstractmethod
import os

from config.stage import settings

from raven.config import IGNORABLE_THRESHOLD_VALUE, TEMPLATE_FORMATE
from raven.utils import template_name_from_class_name, invert_title_case, _title_case


class AbstractResponse(ABC):
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


class BaseResponse(AbstractResponse):
    def __init__(self, *args, **kwargs):
        """
        Instance Variable Description
        -----------------------------

        `threshold_value` --  for rejecting the intent classification which is less than the
        given value.
        `scope` -- this `Dict` object directly received from the Snip engine.
        `response_class` -- 
        """
        # to reject if the probability of intent is less than theshold value.
        self.threshold_value = IGNORABLE_THRESHOLD_VALUE
        self.scope = kwargs["scope"]

        if self.scope is None:
            raise TypeError("scope is passed as empty")

    def render(self, *args, **kwargs):

        self.class_name = kwargs.get("class_name")

        # ## getting file Name
        render_template_name = (
            f"_{invert_title_case(self.class_name)}.{TEMPLATE_FORMATE}"
        )
        # ## sub path from the html/txt file
        render_template_name = (
            f"_{invert_title_case(self.class_name)}/{render_template_name}"
        )
        render_template_name = f'{kwargs.get("sub_path")}/{render_template_name}'
        self.render_template = settings.render_template.get_template(
            render_template_name
        )

    def get_class_name(self):
        raise NotImplementedError("get_class_name must be implemented")

    def check_intent_name(self, name):
        return name.startswith(f"{self.get_class_name()}Intent")

    def get_slot_by_name(self, slot_name):
        """
        Get the rawvalue from the scope of the intent engine.
        """

        for slot in self.scope["slots"]:
            if slot["slotName"] == slot_name:
                return slot["rawValue"]
