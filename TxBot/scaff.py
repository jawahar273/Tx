from subprocess import run
import os

import click

from _scaff.response import gen_response
from _scaff.intent import gen_intent
from _scaff.utils import exit_now

'''
Scaff module helpful in increating the prodicitive of
generating of intent response files.
Scaff module is alway in developer mode as this is a fixed
location.

Intent rules.

1. Always declare intent name ends with '-Intent'(like '-ing' to 'following' from 'follow') in yaml file
before training.
2. Class in response must of Title case with intent name without the suffiex '-Intent'

.. code-block:: yaml
    type: intent
    name: QuitIntent
    $class: Quit


'''

@click.group(invoke_without_command=False)
def main():
    pass



@main.command('intent')
def intent():
    if click.confirm('Do you like generate Intent both?'):
        gen_intent()
    else:
        click.echo('abort!')


@main.command('response')
def response():
    if click.confirm('Do you like generate Response both?'):
        gen_response()
    else:
        click.echo('abort!')


@main.command('both')
def both():
    if click.confirm('Do you like generate Intent and Response both?'):
        temp = gen_intent()
        gen_response(**temp)
    else:
        click.echo('abort!')


@main.command('train')
@click.argument('path', type=click.Path(exists=True),)
@click.option('--name', '-n', default='dataset.json',help='name for the dataset format')
def intent_to_dataset_format(path, name):
    '''
    Folder structure for the intent and dataset.
        storage/
            _profile/
                intents
                dataset

    @params path location of the intent folder and location of dataset folder
    are take from the single arguments.
    '''
    INTENT = 'intents'
    DATASET = 'dataset'

    dataset_path = os.path.join(path, DATASET)
    dataset_file_name = os.path.join(dataset_path, name)

    intent_path = os.path.join(path, INTENT)
    intent_path = os.listdir(intent_path)

    command = 'snips-nlu generate-dataset en'.split()
    command.extend(
            list(map(lambda x: os.path.join(path, INTENT ,x) , intent_path))
    )

    std_out = run(command, capture_output=True)

    click.echo('dataset has been generated and writeing to file..')

    with open(f'{dataset_file_name}', 'w') as dataset_file:
        dataset_file.write(std_out.stdout.decode('utf-8'))

    click.echo('write file successful')



if __name__ == '__main__':
    main()
