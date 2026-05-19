import yaml
from jinja2 import Environment, FileSystemLoader
from netmiko import Netmiko

# Load YAML files
hosts = yaml.load(open('hosts.yml'), Loader=yaml.SafeLoader)
interfaces = yaml.load(open('interfaces.yml'), Loader=yaml.SafeLoader)

# Load Jinja2 template
env = Environment(
    loader=FileSystemLoader('.'),
    trim_blocks=True,
    lstrip_blocks=True
)

template = env.get_template('interfaces_config_template.j2')

# Render config from template
loopback_config = template.render(data=interfaces)

# Loop through devices
for host in hosts["hosts"]:

    net_connect = Netmiko(
        host=host["name"],
        username=host["username"],
        password=host["password"],
        port=host["port"],
        device_type=host["type"]
    )

    print(f"Logged into {host['name']} successfully")

    # Convert config string into list
    config_commands = loopback_config.split("\n")

    output = net_connect.send_config_set(config_commands)

    print(f"Pushed config into {host['name']} successfully")

    net_connect.disconnect()

print("Done!")
