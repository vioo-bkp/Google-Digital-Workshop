def get_hostname_from_row(row):
    hostname_td = row.find('td', class_ = 'hostname')
    hostname_link = hostname_td.find('a')
    hostname = hostname_link.getText()
    return hostname


def get_players_from_row(row):
    players_td = row.find('td', class_ = 'players')
    return players_td.getText()

def get_map_from_row(row):
    map_td = row.find('td', class_ = 'mapname')
    return map_td.getText()

def get_ip_from_row(row):
    ip_td = row.find('td', class_ = None)
    return ip_td.getText()
