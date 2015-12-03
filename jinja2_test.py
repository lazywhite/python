from jinja2 import Environment, FileSystemLoader
import os


PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
        autoescape = False,
        loader = FileSystemLoader(os.path.join(PATH, 'templates')),
        trim_blocks = False)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)


context = {'k1': 'v1', 'k2':'v2'}

print render_template('index.html', context)

## autoescape is disabled default
## manual escaping {{ user.username|e }} 
## is autoescape is enabled, mark expressions as safe{{ user.username|safe }}
