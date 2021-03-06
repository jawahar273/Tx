"""
Scaff module helpful in increating the productive time of
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
rule in traning the intent of
`Snip-NLU <https://snips-nlu.readthedocs.io/en/latest/data_model.html#intent>`_. 
Create a folder and generate sub file with diffrent intent for readbility.

Intent Defining Rules.
''''''''''''''''''''''

.. note::

    the intent file with intent-name are generated automatically.

    .. code-block:: bash

        python scaff.py intent # answer some questions.

1. In-Build folder for saving the intent file is 'raven/Storage'.
2. Following snippet is example after generating of intent from the command line.

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
        # it is highly recommenced don't use underscore as the
        # underscore will automatically added to file name.
        python scaff.py response # answer some questions.



Traning
-------
Converted the intent files into NLU readable/training
formate with help of `SNIP NLU generator`. It is possible to use all the
intent file as a dataset.json.

.. note::

    .. code-block:: bash

        # absolute path must be given.
        python scaff.py train raven/storage/_profile --name dataset.json --dataset dataset

Folder structure for the intent and dataset.

.. code-block:: bash

    storage/
        _profile/
            intents

.. warning::

    Inside storage folder if any intent folder endswith ``?`` then
    they are ignore in traning process. If for example the``_profile?`` 
    intent folder endswith then the this folder will be ignored
    completely by algorithum.


.. note::

    For generating global dataset based on all intent present inside the storage
    folder

    .. code-block:: bash

        # folder contain all intent files
        python scraff.py bot/storage --name dataset.json --dataset dataset

"""

from subprocess import run
import os

import click

from raven.scaff.response import gen_response
from raven.scaff.intent import gen_intent
from raven.scaff.utils import exit_now
from config.stage import settings


@click.group(invoke_without_command=False)
def main():
    pass


@main.command("m2r", help="conver the markdown file into rst extention")
@click.argument("convert_file")
def m2r(convert_file):
    run(f"m2r {convert_file}".split())


@main.command("intent", help="creating the both 'intent' file")
def intent():
    gen_intent()


@main.command("response", help="creating the both 'response' file")
def response():
    gen_response()


@main.command("both", help="creating the both 'response' and 'intents' file")
@click.option(
    "--ipath",
    type=click.Path(exists=True),
    help="base folder give the folder name for saving intents",
)
@click.option(
    "--rpath",
    type=click.Path(exists=True),
    help="base folder give the folder name for saving response",
)
def both(ipath, rpath):
    if click.confirm("Do you like generate Intent and Response both?"):
        if not ipath:
            ipath = "storage"

        temp = gen_intent(ipath)

        if rpath:
            temp["base_path"] = rpath
        gen_response(**temp)
    else:
        click.echo("abort!")


@main.command(
    "train",
    help="\n simply type `raven/storage/` for get starting.\n"
    + "convert list of intent file into train format by giving the folder path `raven/storage/_profile` or `raven/storage/` for train all intent file inside",
)
@click.argument("path", type=click.Path(exists=True))
@click.option(
    "--name", "-n", default="dataset.json", help="name for the dataset format"
)
@click.option(
    "--dataset",
    "-d",
    default=os.path.join("raven", "dataset"),
    help="location for containing the dataset training format `dataset`",
)
@click.option(
    "--common",
    "-g",
    default=os.path.join(settings.DEFAULT_STARTPOINT, "_global"),
    help="global intent will be import into other intents",
)
def intent_to_dataset_format(path: str, name: str, dataset: str, common: str) -> None:
    """
    

    :param path: location of the intent folder and location of dataset folder
        are take from the single arguments.
    :type: path
    :param name: name of the NLU's readable/training format `file` given after generation. default name is `dataset.json` 
    :type: str
    :param dataset: NLU's readable/training format contain `folder` given after generation. default name is `dataset` 
    :type: str
    """
    INTENT = "intents"
    absolute_intent_path = []

    # just renaming to avoid confusion
    dataset_path = dataset

    def generate_intent_path(path: str, INTENT: str, intent_path: str) -> list:
        """
        Get the list of the intent files under `intent` folder inside the given
        folder name.
        """
        return list(map(lambda x: os.path.join(path, INTENT, x), intent_path))

    dataset_file_name = os.path.join(dataset, name)

    true_intent_path = None
    # todo: add all intent based on the path
    import re

    # check given intent path for specific intent folder.
    if not re.match(r".*[_]", path):
        click.echo("get all intents")
        all_dir = os.listdir(path)

        for _path in all_dir:

            if _path.endswith("?"):
                continue
            __intent_path = os.path.join(path, _path, INTENT)
            _intent_path = os.listdir(__intent_path)
            absolute_intent_path.extend(
                generate_intent_path(__intent_path, "", _intent_path)
            )

    else:

        true_intent_path = os.path.join(path, INTENT)
        true_intent_path = os.listdir(true_intent_path)
        absolute_intent_path.extend(
            generate_intent_path(path, INTENT, true_intent_path)
        )

    if common is not False:

        _global_intent = os.listdir(os.path.join(common, INTENT))
        _global_intent = generate_intent_path(common, INTENT, _global_intent)
        absolute_intent_path.extend(_global_intent)

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
