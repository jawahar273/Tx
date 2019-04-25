import os

from utils import invert_title_case as invert_title, _title_case as _title


def gen_response(base_path="TxBot_response", _sub_path=None, _file_name=None):
    f'''
    Automatically generate required files for response
    object inside the `{base_path}`.
    '''

    print('=' * 20, 'Generate Response Files Easy', '=' * 20)
    print(f'The base folder is from `{base_path}`')
    sub_path = _sub_path or input(f'name of the sub folder such as for Example `_task`:')
    # _sub_path = sub_path
    input_path = _file_name or input(f'name of the response file: ')
    file_name = invert_title(input_path)
    input_path = f'_{file_name}'

    try:

        if (os.path.isdir(input_path)):
            input_path = os.path.split(input_path)[0]

        input_path = os.path.join(os.path.split(os.path.dirname(__file__))[0],
                                  base_path, sub_path, input_path)
        os.makedirs(input_path)

    except FileExistsError as e:
        print('Folder already exits')

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
        self.class_name = self.get_class_name()  # class name

        super({_title(file_name)}, self).render(class_name=self.class_name, sub_path='{sub_path}')

        return self.render_template.render()

'''
        file.write(class_template)

    return {
        _sub_path: _sub_path,
        _file_name: _file_name
    }
    print('Response Generated ..')
