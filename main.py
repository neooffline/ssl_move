from logger import logger
import json
from check.local_check import get_days_from_loc_list
from check.remote_check import replace_certs
from scheduler.scheduler import add_job
from scheduler import app
from os import path
from copy_to_remote.copy_to_remote import copy_file
from copy_to_remote.remote_operations import execute

ROOT_DIR_PATH = path.abspath("")

def get_options():
    with open("hosts.json", 'r') as file:
        data = json.load(file)
        hosts = data["hosts"]
        local_cert = data["local"]
        logger.debug(f'Local certs list: {local_cert}\nRemote hosts: {hosts}')
    return hosts, local_cert


def test():
    opts = get_options()
    add_job(replace_certs, params_=opts[0], id_="rem")
    #add_job(get_days_from_loc_list, params_=opts[1], id_="local")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()
    #file_to_copy= ROOT_DIR_PATH + "\\file.txt"
    #copy_file(file_=file_to_copy)
    #execute()
    app.run()
