from jinja2 import Environment, FileSystemLoader
# Load template environment
ENV = Environment(loader=FileSystemLoader('.'))
# Load the template file
template = ENV.get_template("template-task2.j2")
# Create a class for network interfaces
class NetworkInterface(object):

    def __init__(self, name, description, vlan, uplink=True):
        self.name = name
        self.description = description
        self.vlan = vlan
        self.uplink = uplink
# Create interface object
interface_obj = NetworkInterface(
    "GigabitEthernet0/1",
    "Server Port",
    10,
    True
)
# Render template
print(template.render(interface=interface_obj))
