"""
Bot demo only contain the bot module for test as
independent module.
"""

from Bot.Bot_output.cli_output import CLIOutput
from Bot.Bot_input.cli_input import CLIInput

from Bot.Bot_engine.default_engine import DefaultEngine as CommonEngine
from Bot.Bot_layer.preset import layer_list  # predefine layer set.

"""
Global Object:
    output_class, next
Input Object:
    text, input_params
"""
if __name__ == "__main__":

    # mainly useful for CLI front
    # {"tag_remove": "html2text.html2text"}
    engine_param = {
        "dataset_path": "Bot/dataset/dataset.json",
        "next_class": "Bot.Bot_input.cli_input.CLIInput",
        "input_params": {},
        "output_params": {"tag_remove": "html2text.html2text"},
        # 'output_class': 'Bot_output.cli_output.CLIOutput',
        "next": True,
        "is_next": True,
    }

    model = CommonEngine(CLIInput(engine_param), CLIOutput(), engine_param)
    model.add(layer_list)

    while True:

        model.go()
