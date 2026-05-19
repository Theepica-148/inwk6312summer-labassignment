from netmiko import Netmiko

device = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

net_connect = Netmiko(**device)

output = net_connect.send_command(
    "show ip route",
    use_textfsm=True
)

net_connect.disconnect()

print("\nParsed Routing Table (R1)\n")

for route in output:
    protocol = route.get("protocol", "N/A")
    network = route.get("network", "N/A")
    distance = route.get("distance", "N/A")
    metric = route.get("metric", "N/A")

    print(f"Protocol : {protocol}")
    print(f"Network  : {network}")
    print(f"Distance : {distance}")
    print(f"Metric   : {metric}")
    print("-" * 40)
