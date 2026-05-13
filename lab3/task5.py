from jinja2 import Environment, FileSystemLoader
# Load environment
ENV = Environment(loader=FileSystemLoader('.'))
# Load template
template = ENV.get_template("template-task5.j2")
# List of interfaces
inter_list = [
    "GigabitEthernet0/1",
    "GigabitEthernet0/2",
    "GigabitEthernet0/3"
]
# Render template
print(template.render(interface_list=inter_list))
