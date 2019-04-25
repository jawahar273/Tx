
import click

from _scaff.response import gen_response
from _scaff.intent import gen_intent
from _scaff.utils import exit_now 

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



click.echo('If needed both intent and response use --both arguments.' )

@click.command()
@click.option('--intent', '-i',default=False, type=bool,
              help='Generate Intent file.')
@click.option('--response', '-r', default=False, type=bool,
              help='Generate Response folder.')
@click.option('--both', '-b', default=False, type=bool,
              help='Generate Intent and Response folder')
# @click.option('--loop', '-l', default=False,
#               help='Loop through the process')
def  main(intent, response, both):

    if intent:
        if click.confirm('Do you want to continue with generation of intent only?'):
            gen_intent()
    elif response:
        if click.confirm('Do you want to continue with generation of response only?'):
            gen_response()
    elif both:
        temp = gen_intent()
        gen_response(**temp)
    else:
        click.echo('Check you arguments')        

if __name__ == '__main__':
    main()