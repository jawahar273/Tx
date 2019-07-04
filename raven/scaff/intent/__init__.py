import os

from jinja2 import Template
from click import confirm
from pathlib import Path

from raven.utils import invert_title_case as invert_title, _title_case as _title
from raven.scaff.utils import exit_now
from config.stage import settings


def gen_intent(base_path="storage"):
    f"""
    Automatically generate required files for intent
    object inside the `{base_path}/intents`.
    """
    print("*" * 20, "Generate Intent yaml Files Easy", "*" * 20)

    sub_path = input(f"Create a sub folder under the '{base_path}': ")
    sub_path = f"_{sub_path}"
    # to keep the original value of the folder given by the user
    _sub_path = sub_path
    # sub folder is always contant as `intent`
    sub_path = os.path.join(sub_path, "intents")
    file_name = input("name of the intent file: ")
    _file_name = file_name
    scaff_path = invert_title(file_name)

    try:
        sub_path = os.path.join(
            os.path.dirname(settings.DEFAULT_STARTPOINT), base_path, sub_path
        )

        os.makedirs(sub_path)

    except FileExistsError as e:
        print("Folder already exits")

    scaff_path = os.path.join(sub_path, scaff_path)
    scaff_path = f"{scaff_path}.yml"

    print("abs folder", sub_path)
    print("If something is wrong, press 1  to exit or press any key")
    if input("..") == "1":
        exit_now()

    def generate_files(file_name, sub_path):

        with open(scaff_path, "w") as intent_file:

            file_name = invert_title(invert_title(file_name))

            intent_file_template = None  # Template(intent_file.read())
            template_py = os.path.join(os.path.dirname(__file__), "template.yml.html")
            with open(template_py) as template:
                intent_file_template = Template(template.read())
            intent_file.write(
                intent_file_template.render(
                    file_name=file_name, _title=_title, sub_path=_sub_path
                )
            )
            print("Intent generated..")

    if not Path(scaff_path).is_file():

        generate_files(file_name, sub_path)

    elif confirm("file exsit, do like to override the exsits files"):
        # print('file exit, recheck you generating name and check do you need the file')
        generate_files(file_name, sub_path)

    return {"_sub_path": _sub_path, "_file_name": _file_name}
