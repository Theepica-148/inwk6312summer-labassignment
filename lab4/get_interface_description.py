from netmiko import ConnectHandler

# Router 1
r01 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.101",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# Router 2
r02 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.102",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# Router 3
r03 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.103",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# Router 4
r04 = {
    "device_type": "cisco_ios",
    "ip": "192.168.1.104",
    "username": "student",
    "password": "Meilab123",
    "port": 22
}

# Loop through routers
for device in (r01, r02, r03, r04):

    # Connect to device
    net_connect = ConnectHandler(**device)

    # Execute command
    output = net_connect.send_command("show interface description")

    # Disconnect
    net_connect.disconnect()

    # Print output
    print("-" * 100)
    print(f"Interface Description for {device['ip']}")
    print("-" * 100)

    print(output)

    print("-" * 100)
