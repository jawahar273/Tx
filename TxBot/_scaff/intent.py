import os

from utils import invert_title, _title


def gen_intent(base_path='storage'):
    f'''
    Automatically generate required files for intent
    object inside the `{base_path}/intents`.
    '''
    print('*' * 20, 'Generate Intent yaml Files Easy', '*' * 20)

    sub_path = input('inside the storage sub folder name such as `_task`: ')
    _sub_path = sub_path
    # sub folder is always contant as `intent`
    sub_path = os.path.join(sub_path, 'intents')
    file_name = input('name of the intent file: ')
    _file_name = file_name
    scaff_path = invert_title(file_name)

    try:
        sub_path = os.path.join(os.path.split(os.path.dirname(__file__))[0],
                                base_path, sub_path)
        os.makedirs(sub_path)

    except FileExistsError as e:
        print('Folder already exits')

    scaff_path = os.path.join(sub_path, scaff_path)
    scaff_path = f'{scaff_path}.yml'

    print('abs folder', scaff_path)
    print('If somthing is wrong, press 1  to exit or press any key')
    if input('..') == '1':
        exit_now()

    def generate_files(file_name):
        with open(scaff_path, 'w') as intent_file:

            file_name = invert_title(invert_title(file_name))
            intent_file_template = f'''
#  {file_name} desc
---
type: intent
name: {file_name}Intent
$class: {_title(file_name)}
utterances:
    - sm
'''
            intent_file.write(intent_file_template)
            print('Intent generated..')

    if not os.path.isfile(scaff_path):

        generate_files(file_name)

    else:
        print('file exit, recheck you generating name and check do you need the file')

    return {
        '_sub_path': _sub_path,
        '_file_name': _file_name
    }
