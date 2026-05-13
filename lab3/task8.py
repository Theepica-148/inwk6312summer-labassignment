# Import Jinja2 library and PyYAML
from jinja2 import Environment, FileSystemLoader
import yaml
# Declare template environment
ENV = Environment(loader=FileSystemLoader('.'))
# Create custom filter function
def get_interface_speed(interface_name):
    """
    Returns default Mbps speed based on interface name
    """

    if 'gigabit' in interface_name.lower():
        return 1000

    if 'fast' in interface_name.lower():
        return 100

    return "Unknown"
# Register custom filter with Jinja
ENV.filters['get_interface_speed'] = get_interface_speed
# Load template
template = ENV.get_template("template-task8.j2")
# Load YAML data
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)
# Render template
print(template.render(interface_list=interfaces))
