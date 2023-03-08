from logger import logger
import json
from check.local_check import get_days_from_loc_list
from check.remote_check import get_days_from_rem_list
from scheduler.scheduler import add_job
from scheduler import app

with open("hosts.json", 'r') as file:
    data = json.load(file)
    hosts = data["hosts"]
    local_cert = data["local"]
    logger.debug(f'Local certs list: {local_cert}\nRemote hosts: {hosts}')


def test():
    add_job(get_days_from_loc_list, params_=local_cert, id_="local")
    add_job(get_days_from_rem_list, params_=hosts, id_="rem")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
    app.run()
