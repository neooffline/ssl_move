from paramiko import SSHClient
from os.path import abspath
from logger import logger

ROOT_DIR_PATH = abspath("")


def execute(): 
    p_key = ROOT_DIR_PATH + '\..\.ssh\id_rsa'
    known_hosts = ROOT_DIR_PATH + '\..\.ssh\known_hosts'
    ssh = SSHClient()
    ssh.load_system_host_keys(known_hosts)
    ssh.connect(hostname='neooffline.ru', port=3322, username='homesrv', key_filename=p_key)
    command = """
    sudo service qbittorrent restart
    sudo service webmin restart
    """

    stdin_, stdout_, stderr_ = ssh.exec_command(command)
    stdout_.channel.recv_exit_status()
    lines = stdout_.readlines()
    logger.debug(f'Result: {lines}')

    ssh.close()

