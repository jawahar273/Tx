"""
The default layer are defined but need to import first.
"""


from raven.layer.cmd.wiki import WikiLayer

# intergating diffrent layer
layer_list = [WikiLayer({})]
