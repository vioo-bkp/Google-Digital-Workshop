import json
from web_scrapper_handlers.facade import get_servers


def main():
    servers = get_servers()
    servers_dict = list(map(lambda server: server.__dict__, servers))
    with open('servers_info.json', 'w+') as json_file:
        json.dump(servers_dict, json_file)


if __name__ == '__main__':
    main()
