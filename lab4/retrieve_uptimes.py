from netmiko import Netmiko

# List of routers
devices = [

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
        "port": 22,
    }

]

# Loop through all routers
for device in devices:

    print("\n===================================")
    print(f"Connecting to {device['ip']}")

    # Connect to router
    net_connect = Netmiko(**device)

    # Execute command
    output = net_connect.send_command("show version")

    # Disconnect
    net_connect.disconnect()

    # -----------------------------
    # Extract uptime
    # -----------------------------
    uptime_index = output.find("uptime is")

    if uptime_index != -1:

        uptime_line = output[uptime_index:].split("\n")[0]

        print(f"Uptime: {uptime_line}")

    # -----------------------------
    # Extract Configuration Register
    # -----------------------------
    config_index = output.find("Configuration register")

    if config_index != -1:

        config_line = output[config_index:].split("\n")[0]

        print(f"{config_line}")
