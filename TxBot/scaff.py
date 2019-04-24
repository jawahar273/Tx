import os
from utils import invert_title, _title

'''
Scaff module helpful in increating the prodicitive of
generating of intent response files.

Intent rules.

1. Always declare intent name ends with '-Intent'(like '-ing' to 'following' from 'follow') in yaml file
before training.
2. Class in response must of Title case with intent name without the suffiex '-Intent'

.. code-block:: yaml
    type: intent
    name: QuitIntent
    $class: Quit


'''


def exit_now():
    print('good bye..')
    exit(0)


def gen_response(base_path="TxBot_response"):

    print('*' * 20, 'Generate Response Files Easy', '*' * 20)
    print(f'The base folder is from `{base_path}`')
    sub_path = input(f'name of the sub folder such as for Example `_task`:')
    input_path = input(f'name of the intent file for response: ')
    file_name = invert_title(input_path)
    input_path = f'_{input_path}'

    try:

        if (os.path.isdir(input_path)):
            input_path = os.path.split(input_path)[0]

        input_path = os.path.join(os.path.dirname(__file__),
                                  base_path, sub_path, input_path)
        os.makedirs(input_path)

    except FileExistsError as e:
        print('Folder already exits')
        exit_now()

    scaff_path = os.path.join(input_path, file_name)
    print('abs folder', scaff_path)
    print('If somthing is wrong, press 1  to exit or press any key')
    if input('..') == '1':
        exit_now()

    with open(f'{scaff_path}.html', 'w') as file:
        pass

    with open(f'{scaff_path}.txt', 'w') as file:
        pass

    with open(f'{scaff_path}.py', 'w') as file:
        class_template = f'''
from TxBot_response.abstract_response import TxBaseResponse


class {_title(file_name)}(TxBaseResponse):

    def __init__(self):
        super({_title(file_name)}, self).__init__(self)

    def get_class_name(self):
        return self.__class__.__name__

    def render(self):
        pass

        '''
        file.write(class_template)

    print('done..')


print_text = '''
0. Exit
1. Help
2. Generate response
'''

print('press 1 for help.')
from sys import exit

while True:

    user_number = int(input('command: '))
    if user_number == 0:
        exit_now()

    elif user_number == 1:
        print(print_text)

    elif user_number == 2:
        gen_response()
