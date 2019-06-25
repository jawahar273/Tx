"""
Engine module is used for higher level or specific object
purpose. Handle them with care.
"""

from Bot.config import STOPLAYER
from Bot.utils import import_class


class AbstractEngine:

    def __init__(self, *args, **kwarg):

        raise NotImplementedError("`__init__` is not implemented")

    def add(self, layer):

        raise NotImplementedError("add() is not implemented")

    def go(self, *args, **kwarg):

        raise NotImplementedError("go() is not implemented")


class BaseEngine(AbstractEngine):
    """
    Base engine will be mother of all its sub-class. As
    major lifting is taken in inside the `BaseEngine`. Just
    use the sub-class to handline the case which Mother's
    class can't be handling.
    """

    def __init__(self, input_object, output_object, engine_param=None):
        """
        Engine will be intermediate object between the input
        and output object.
        All the layer must be set using
        .. py:method:: BaseEngine.add(layers) Engine class.

        ..note
        1. get the value from input object using the function
        """
        self.input_object = input_object
        self.output_object = output_object
        self.engine_param = engine_param
        self.layers = []
        # Return object is the main point
        # in engine object.
        self.return_object = None
        self.break_layer = False
        self.engine_name = "base_engine"
        output_params = engine_param.get("output_params")
        self.output_object.params(output_params)
        STOPLAYER.connect(self.subscribe_tobreak)
        # return object is alway for accessing
        # processed input inside.

    def add(self, layer):

        assert layer, "None type is not allowed"
        if isinstance(layer, list):
            self.layers.extend(layer)
        else:
            self.layers.append(layer)

    def subscribe_tobreak(self, sender):
        """
        Get the event signal and return true(for now).
        """
        self.break_layer = True

    def go(self):
        """ Running the go function which will be used
        to run.
        Return is layer, will handling the input sentence.

        ..notes ::
            sub class must return `self.return_object` itself.
            Returning to ` OutPut` module must decised by ` Engine`.
        """

        if len(self.layers) == 0:
            raise ValueError("Layer is empty, add some function layer for processing.")
        self.return_object = self.input_object.processed()

        for single_layer in self.layers:
            self.return_object = single_layer.response(self.return_object)

            if self.break_layer:
                break

    def to_output(self, txObject):
        self.break_layer = False

        # OutPut Object are called here.
        # This must be changed in sub class.

        return self.output_object.output(self.return_object)

    def next(self):
        """
        .. py:method:: BasedEngine.next() are recommented to be called after the end
        of :class:method
        """

        if self.engine_param["is_next"]:
            self.input_object = import_class(self.engine_param["next_class"])(
                self.engine_param
            )
        self.return_object = None
