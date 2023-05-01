from paramiko import SSHClient
from scp import SCPClient
from logger import logger
from os.path import abspath


ROOT_DIR_PATH = abspath("")

def copy_file(file_): 
    p_key = ROOT_DIR_PATH + '\..\.ssh\id_rsa'
    known_hosts = ROOT_DIR_PATH + '\..\.ssh\known_hosts'
    ssh = SSHClient()
    ssh.load_system_host_keys(known_hosts)
    ssh.connect(hostname='neooffline.ru', port=3322, username='homesrv', key_filename=p_key)

    with SCPClient(ssh.get_transport()) as scp:
        logger.debug(f'Try put file: {file_}')
        scp.put(files=file_, remote_path='/opt/ssl/')
    ssh.close()