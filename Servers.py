# servers.py

class Servers:
    def __init__(self):
        # Initializing an empty list of servers
        self.servers = []

    def connect_to_servers(self):
        # Method to connect to the servers
        print("Connecting to servers...")
        self.servers = ["Server 1", "Server 2"]  # Simulating two servers

    def manage_server(self, server_id):
        # Method to manage a specific server
        print(f"Managing server {server_id}")
