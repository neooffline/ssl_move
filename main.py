from logger import logger
import json
from check.local_check import get_days_from_loc_list
from check.remote_check import get_days_from_rem_list
from scheduler.scheduler import add_job
from scheduler import app


def get_options():
    with open("hosts.json", 'r') as file:
        data = json.load(file)
        hosts = data["hosts"]
        local_cert = data["local"]
        logger.debug(f'Local certs list: {local_cert}\nRemote hosts: {hosts}')
    return hosts, local_cert


def test():
    opts = get_options()
    add_job(get_days_from_rem_list, params_=opts[0], id_="rem")
    add_job(get_days_from_loc_list, params_=opts[1], id_="local")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
    app.run()
