import ssl
import OpenSSL
from logger import logger
from datetime import datetime, timedelta
from check.compare import expires_days
from copy_to_remote.copy_to_remote import copy_file
from copy_to_remote.remote_operations import execute
from certs.files import get_files_to_copy
from os.path import abspath


def remote_cert_until(uri_: str, port_: ...):
    if not port_:
        port_ = 443
    #logger.debug(f'port:{port_}')
    try:
        cert = ssl.get_server_certificate((uri_, port_))
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        tt = x509.get_notAfter().decode("UTF-8").strip('Z') + '.000000'
        return datetime.strptime(tt, '%Y%m%d%H%M%S.%f')
    except Exception as ex:
        logger.error(f'Error to response certificate:{ex}')
        return datetime.now()


def get_days_from_rem_list(hosts_: dict):
    day_off= []
    for h in hosts_:
        until_ = remote_cert_until(h, hosts_.get(h))
        days = expires_days(until_)
        logger.debug(f'For host: {h}:{hosts_.get(h)} have {days} day(s) untill expire')
        day_off.append({h:days})  
    return day_off    

def replace_certs(hosts_: dict):
    for ele in get_days_from_rem_list(hosts_=hosts_):
        for keys in ele:
            logger.debug(f'Now check: {keys}, value {ele.get(keys)}')
            if ele.get(keys) <= 83:
                for file in get_files_to_copy(): 
                    logger.debug(f'Copying file: {file}')#, abs_path {abspath(file)}')
                    copy_file(file_=file)
            else:
                logger.debug(f'For host {keys} nowhing to do')