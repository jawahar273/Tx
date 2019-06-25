import os

from jinja2 import Template
from click import confirm

from Bot.utils import invert_title_case as invert_title, _title_case as _title
from Bot.scaff.utils import exit_now


def gen_response(base_path="Bot_response", _sub_path=None, _file_name=None):
    f"""
    Automatically generate required files for response
    object inside the `{base_path}`.
    """

    print("=" * 20, "Generate Response Files Easy", "=" * 20)
    print(f"The base folder is `{base_path}`")
    sub_path = _sub_path or input(
        f"name of the sub folder such as for Example `_task`:"
    )
    if(not sub_path.startswith('_')):
        sub_path = f'_{sub_path}'
    # _sub_path = sub_path
    input_path = _file_name or input(f"name of the response file: ")
    file_name = invert_title(input_path)
    input_path = f"_{file_name}"
    template_scaff_path = None

    try:

        template_scaff_path = os.path.join(
            os.path.dirname("Bot/storage"),
            base_path,
            "templates",
            sub_path,
            input_path,
            input_path,
        )
        input_path = os.path.join(
            os.path.dirname("Bot/storage"), base_path, sub_path, input_path
        )

        if not confirm("Files may be overridden. Still do like to continue"):
            exit_now()

        os.makedirs(input_path)

    except FileExistsError as e:

        print(f"Just kidding look like the folder already exit in: {input_path}")

    try:

        # split the path to avoid sub folder.
        os.makedirs(os.path.split(template_scaff_path)[0])

    except FileExistsError as e:

        print("Template Folder already exits")

    py_scaff_path = os.path.join(input_path, file_name)
    print("abs folder", input_path)

    with open(f"{py_scaff_path}.py", "w") as file:

        class_template = None  # Template(intent_file.read())
        template_py = os.path.join(os.path.dirname(__file__), "template.py.html")
        with open(template_py) as template:
            class_template = Template(template.read())

        file.write(
            class_template.render(file_name=file_name, sub_path=sub_path, _title=_title)
        )

    with open(f"{template_scaff_path}.html", "w") as file:
        template_ = os.path.join(os.path.dirname(__file__), "template.html.html")
        with open(template_) as template:
            file.write(template.read())

    return {_sub_path: _sub_path, _file_name: _file_name}
    print("Response Generated ..")
