"""
Bot demo only contain the bot module for test as
independent module.
"""

from raven.output.cli_output import CLIOutput
from raven.input.cli_input import CLIInput

from raven.engine.default_engine import DefaultEngine as CommonEngine
from raven.layer.preset import layer_list  # predefine layer set.

if __name__ == "__main__":

    # mainly useful for CLI front
    # {"tag_remove": "html2text.html2text"}
    engine_param = {
        "dataset_path": "raven/dataset/dataset.json",
        "next_class": "raven.input.cli_input.CLIInput",
        "input_params": {},
        "output_params": {"tag_remove": "html2text.html2text"},
        # 'output_class': 'output.cli_output.CLIOutput',
        "next": True,
        "is_next": True,
    }

    model = CommonEngine(CLIInput(engine_param), CLIOutput(), engine_param)
    model.add(layer_list)

    while True:

        model.go()
