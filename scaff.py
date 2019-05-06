"""
Scaff module helpful in increating the prodicitive of
generating of intent response files.
Scaff should be used alway in developer times as this functional
depend fixed location.

.. code-block:: bash

    # don't know what to do type this command.
    python scraff.py --help 


Intent
------

Intent is a description for chatbot which describe
the given text/voice. The intent designers must follow
rule in traning the intent of `Snip-NLU <https://snips-nlu.readthedocs.io/en/latest/data_model.html#intent>`_. 
Create a folder and generate sub file with diffrent intent for readbility.

Intent Defining Rules.
''''''''''''''''''''''

.. note::

    the intent file with intent-name are generated automatically.

    .. code-block:: bash

        python scaff.py intent # answer some questions.

1. Always declare intent name ends with '-Intent and along with sub folder name Example `BioIntent_profile`.
2. Class in response must of Title case with intent name without the suffiex '-Intent'(optional)
3. In-Build folder for saving the intent file is 'bot/Storage'.

.. code-block:: yaml

    type: intent
    name: pwnedIntent_global
    # `pwned` is the intent name
    # `Intent` must be present at the end of the intent name
    # `_global` is the sub folder where this intent is present


Response
--------

Response is like action planner. After getting the intent
classification the response will execute its given action
and return the html parse structural text.

Response Defining Rules.
''''''''''''''''''''''''

.. note::

    the response and template file are generate automatically.

    .. code-block:: bash

        # In place of choosing the file name,
        # it is highly recommented don't use underscore as the
        # underscore will automatically added to file name.
        python scaff.py response # answer some questions.


1. The response file must align with intent file that is the name of the response
must be same as the intent file. Such example is `Bot_response/_global/_pwned` and template
`Bot_response/templates/_global/_pwned/_pwned.html` is equallent to `storage/_global/intents/pwned.yml`


Click Commands functions
------------------------

"""

from subprocess import run
import os

import click

from Bot.scaff.response import gen_response
from Bot.scaff.intent import gen_intent
from Bot.scaff.utils import exit_now


@click.group(invoke_without_command=False)
def main():
    pass


@main.command("m2r")
@click.argument("convert_file")
def m2r(convert_file):
    run(f"m2r {convert_file}".split())


@main.command("intent")
def intent():
    gen_intent()


@main.command("response")
def response():
    gen_response()


@main.command("both")
def both():
    if click.confirm("Do you like generate Intent and Response both?"):
        temp = gen_intent()
        gen_response(**temp)
    else:
        click.echo("abort!")


@main.command(
    "train",
    help="convert list of intent file into train format by giving the folder path `Bot/storage/_profile`",
)
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--name", "-n", default="dataset.json", help="name for the dataset format"
)
@click.option(
    "--dataset",
    "-d",
    default=os.path.join("Bot", "storage"),
    help="location for containing the dataset training format `dataset`",
)
@click.option(
    "--common",
    "-g",
    default=os.path.join("Bot", "storage", "_global"),
    help="global intent will be import into other intents",
)
def intent_to_dataset_format(path: str, name: str, dataset: str, common: str) -> None:
    """
    Converted the intent files into NLU readable/training
    formate with help of `SNIP NLU generator`.

    .. note::

        .. code-block:: bash

            # absolute path must be given.
            python scaff.py train Bot/storage/_profile --name dataset.json --dataset dataset

    Folder structure for the intent and dataset.

    .. code-block:: bash

        storage/
            _profile/
                intents
                dataset  # manully create this folder.

    :param path: location of the intent folder and location of dataset folder
        are take from the single arguments.
    :type: path
    :param name: name of the NLU's readable/training format file given after generation. default name is `dataset.json` 
    :type: str
    :param dataset: NLU's readable/training format contain folder given after generation. default name is `dataset` 
    :type: str
    """
    INTENT = "intents"
    absolute_intent_path = []
    # DATASET = "dataset"

    # path = os.path.join(DEFAULT_STARTPOINT, path)
    # dataset_path = os.path.join(dataset_path, DATASET)

    # just renaming to avoid confusion
    dataset_path = dataset

    def generate_intent_path(path: str, INTENT: str, intent_path: str) -> list:
        """
        Get the list of the intent files under `intent` folder inside the given
        folder name.
        """

        return list(map(lambda x: os.path.join(path, INTENT, x), intent_path))

    dataset_file_name = os.path.join(dataset, name)

    true_intent_path = os.path.join(path, INTENT)
    true_intent_path = os.listdir(true_intent_path)

    absolute_intent_path = generate_intent_path(path, INTENT, true_intent_path)

    if common is not False:

        _global_intent = os.listdir(os.path.join(common, INTENT))
        _global_intent = generate_intent_path(common, INTENT, _global_intent)
        absolute_intent_path.extend(_global_intent)

    import IPython

    IPython.embed()
    command = "snips-nlu generate-dataset en".split()
    command.extend(absolute_intent_path)

    std_out = run(command, capture_output=True)
    click.echo("dataset has been generated and writting to file..")

    if std_out.stdout == b"":
        click.echo(std_out.stderr.decode("utf-8"))
        exit_now()

    with open(f"{dataset_file_name}", "w") as dataset_file:
        dataset_file.write(std_out.stdout.decode("utf-8"))

    click.echo("write file successful")


if __name__ == "__main__":
    main()
