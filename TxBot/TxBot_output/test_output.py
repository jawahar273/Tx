from .abstract_output import TxBaseOutput


class TxSampleTestOutput(TxBaseOutput):

    def __init__(self):
        super(TxSampleTestOutput, self).__init__()

    def output(self, for_output):
        super(TxSampleTestOutput, self).output(for_output)
        print('output ...', for_output)

        if for_output['next']:
            self.next(for_output)

    def next(self, to_input):
        import IPython;IPython.embed()
        
        super(TxSampleTestOutput, self).next(to_input)
