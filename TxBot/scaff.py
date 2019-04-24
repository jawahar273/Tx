import os

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

def gen_response(base_path = "TxBot_response"):

    input_path = input(f'name of the file and path from `{base_path}`: ')
    scaff_path = input_path
    input_path = f'_{input_path}'

    try:

        if (os.path.isdir(input_path)):
            input_path = os.path.split(input_path)[0]

        input_path = os.path.join(os.path.dirname(__file__), base_path, input_path)
        os.mkdir(input_path)

    except FileExistsError as e:
        pass

    scaff_path = os.path.join(input_path, scaff_path)

    with open(f'{scaff_path}.html', 'w') as file:

        file.close()

    with open(f'{scaff_path}.txt', 'w') as file:

        file.close()

    with open(f'{scaff_path}.py', 'w') as file:

        file.close()


print_text = '''
1. help
2. Generate response
'''

user_number = int(input('command: '))
print('press 1 for help.')
if user_number == 1:
    print(print_text)
elif user_number == 2:
    gen_response()



