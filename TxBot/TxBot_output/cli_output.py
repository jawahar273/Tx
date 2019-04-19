from colorama import init
from termcolor import colored

init()


from .abstract_output import TxBaseOutput
from TxBot_input.cli_input import CLIInput
from config import SKIP_OUTPUT, FOR_OUTPUT


class CLIOutput(TxBaseOutput):
    def __init__(self, txObject=None):

        super(CLIOutput, self).__init__(txObject)

    def output(self, txObject):

        temp = super(CLIOutput, self).output(txObject)

        print(colored("Tx#> ", "blue"), "\n", colored(temp, "white"))
        # if for_output['next']:
        #     self.next(for_output)

    # def next(self, to_input):
    #     """
    #     next() function is called as repeating actions.
    #     input_class.next() and output_class.next()
    #     are interconneccted as intermediate.
    #     """
    #     print("calling next: output")

    #     super(CLIOutput, self).next(to_input)

    #     # self.next_fun.next(to_input)
