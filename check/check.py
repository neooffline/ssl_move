import json
import ssl
import OpenSSL
from logger import logger
from datetime import datetime, timedelta


def local_cert_until(location_: str):
    with open(location_, 'rb') as cert_b:
        cert_ = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_b.read())
        tt = cert_.get_notAfter().decode("UTF-8").strip('Z') + '.000000'
    return datetime.strptime(tt, '%Y%m%d%H%M%S.%f')


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
        return datetime.now( )


def expires_days(expires_):
    return (expires_ - datetime.now()).days


def get_days_from_rem_list(hosts_: dict):
    for h in hosts_:
        until_ = remote_cert_until(h, hosts_.get(h))
        days = expires_days(until_)
        logger.debug(f'For host: {h}:{hosts_.get(h)} have {days} day(s) untill expire')


def get_days_from_loc_list(local_: list):
    for ele_ in local_:
        logger.debug(f'Current location for cert: {ele_}')
        until_ = local_cert_until(ele_)
        days = expires_days(until_)
        logger.debug(f'For cert in location {ele_} have {days} day(s) untill expire')


with open("../hosts.json", 'r') as file:
    data = json.load(file)
    hosts = data["hosts"]
    local_cert = data["local"]
    logger.debug(f'Local certs list: {local_cert}\nRemote hosts: {hosts}')


#get_days_from_list(hosts_=hosts)
get_days_from_loc_list(local_cert)
#logger.info(f'for neooffline days: {get_days_from_list(hosts)}')
