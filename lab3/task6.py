from jinja2 import Environment, FileSystemLoader
# Load Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))
# Load template
template = ENV.get_template("template-task6.j2")
# List of interface dictionaries
interfaces = [
    {
        "name": "GigabitEthernet0/1",
        "desc": "uplink port",
        "uplink": True
    },
    {
        "name": "GigabitEthernet0/2",
        "desc": "Server port number one",
        "vlan": 10
    },
    {
        "name": "GigabitEthernet0/3",
        "desc": "Server port number two",
        "vlan": 10
    }
]
# Render template
print(template.render(interface_list=interfaces))
