from jinja2 import Environment, FileSystemLoader
# Load environment
ENV = Environment(loader=FileSystemLoader('.'))
# Load template
template = ENV.get_template("template-task4.j2")
# Network interface class
class NetworkInterface(object):

    def __init__(self, description, vlan):
        self.description = description
        self.vlan = vlan
# Create interface object
interface_obj = NetworkInterface(
    "Server Port",
    10
)
# Render template
output = template.render(interface=interface_obj)

print(output)
