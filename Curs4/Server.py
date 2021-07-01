class Server:
    def __init__(self, hostname, players, map_name, ip):
        self.hostname = hostname
        self.players = players
        self.map_name = map_name
        self.ip = ip

    def __str__(self):
        return f'Nume: {self.hostname}\nNumar jucatori: {self.players}\nMap: {self.map_name}\nIP: {self.ip}\n\n'
