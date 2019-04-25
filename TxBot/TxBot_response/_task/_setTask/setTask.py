from os.path import isfile

from TxBot_response.abstract_response import TxBaseResponse
from utils import windows_path_regex


class SetTask(TxBaseResponse):

    def __init__(self):
        super(SetTask, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def check_intent_name(self, name):
        return super().check_intent_name(name)

    def render(self, snip_scope):
        '''
        .. code-block:: yaml
                error_code:
                    - class_name-file:error in uploading of file 

        @params snip_scope :method: `SnipsNLUEngine.parse` return value are passed arguments
        @type Dict
        '''
        respone_data = []

        if not self.check_intent_name(slots['intentName']):
            # log for wrong intent class
            print('wrong intent')
            return self.default_response

        slots = snip_scope['slots']

        for slot in slots:
            file_name = slot['file_name']

            if not isfile(file_name):
                respone_data.append({
                    'errorCode': f'{self.get_class_name()}-file',
                    'errorMsg': 'Check the file before uploading',
                })

            if not windows_path_regex(slots['file_name']):
                # in NLU engine the root path will be remove
                # automatically so the root will be added.
                file_name = f'/{file_name}'

            with open(file_name) as task_file:

                # read the give file
                temp_pointer = task_file.read()

