from jinja2 import Environment, FileSystemLoader, select_autoescape


render_template = Environment(
    loader=FileSystemLoader(['Tx/templates', 'TxBot/TxBot_response/']),
    autoescape=select_autoescape(['html', 'xml'])
)

