from jinja2 import Environment, FileSystemLoader
# Load environment
ENV = Environment(loader=FileSystemLoader('.'))
# Load template
template = ENV.get_template("template-task5a.j2")
# Dictionary of interfaces
inter_dict = {
    "GigabitEthernet0/1": "Server port number one",
    "GigabitEthernet0/2": "Server port number two",
    "GigabitEthernet0/3": "Server port number three"
}
# Render template
print(template.render(interface_dict=inter_dict))
