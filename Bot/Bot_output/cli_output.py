# @maintenance mode

from colorama import init
from termcolor import colored

init()

from .abstract_output import BaseOutput


class CLIOutput(BaseOutput):

    def __init__(self, txObject=None):

        super(CLIOutput, self).__init__(txObject)

    def output(self, txObject):

        temp = super(CLIOutput, self).output(txObject)

        print(colored("Tx#> ", "blue"), colored(temp, "white"))
