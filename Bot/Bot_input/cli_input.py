from colorama import init
from termcolor import colored

init()

from .abstract_input import BaseInput


class CLIInput(BaseInput):
    def __init__(self, txObject=None):

        txObject.update({"text": input(colored("Tx#> ", "green"))})

        super(CLIInput, self).__init__(txObject)

    # def cinit(self, to_input):
    #     """
    #     `cinit` for better interaction with sys.inputs
    #     and for calling inside `next()`.
    #     `input params` must be defined in yaml/json as config file.
    #     """

    #     to_input.update(to_input)

    #     super(CLIInput, self).pre_loading_set(to_input)
    #     self.processed()

    def processed(self):

        super(CLIInput, self).processed()
        return self.return_object
