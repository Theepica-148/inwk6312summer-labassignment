from netmiko import Netmiko

# List of devices
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.101",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.102",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.103",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    },

    {
        "device_type": "cisco_ios",
        "ip": "192.168.1.104",
        "username": "student",
        "password": "Meilab123",
        "secret": "cisco",
        "port": 22,
    }
]

# Loop through all routers
for device in devices:

    print(f"\nConnecting to {device['ip']}")

    # Connect to router
    net_connect = Netmiko(**device)

    # Show default prompt
    print(f"Default prompt: {net_connect.find_prompt()}")

    # Disable mode
    net_connect.send_command_timing("disable")
    print(f"Disable command: {net_connect.find_prompt()}")

    # Enable mode
    net_connect.enable()
    print(f"Enable command: {net_connect.find_prompt()}")

    # Disconnect session
    net_connect.disconnect()
