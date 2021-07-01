from web_scrapper_handlers.scrapper import *
from web_scrapper_handlers.data_extractor import *
from Server import Server


def get_servers_info():
    url = 'https://www.game-state.com/index.php?game=samp&location=RO'
    page = get_page_html(url)
    table_rows = get_table_rows(page)

    servers = []

    for row in table_rows:
        servers.append(
            (get_hostname_from_row(row), get_players_from_row(row), get_map_from_row(row), get_ip_from_row(row)))

    return servers


def convert_touple_to_object(info):
    hostname = info[0]
    players = info[1]
    map = info[2]
    ip = info[3]

    return Server(hostname, players, map, ip)


def get_servers():
    servers_info = get_servers_info()
    return list(map(convert_touple_to_object, servers_info))
