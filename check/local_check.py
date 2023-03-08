import OpenSSL
from check.compare import expires_days
from logger import logger
from datetime import datetime, timedelta


def local_cert_until(location_: str):
    logger.debug(f'Working with file: {location_}')
    with open(location_, 'rb') as cert_b:
        cert_ = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert_b.read())
        tt = cert_.get_notAfter().decode("UTF-8").strip('Z') + '.000000'
    return datetime.strptime(tt, '%Y%m%d%H%M%S.%f')


def get_days_from_loc_list(local_: list):
    for ele_ in local_:
        logger.debug(f'Current location for cert: {ele_}')
        until_ = local_cert_until(ele_)
        days = expires_days(until_)
        logger.debug(f'For cert in location {ele_} have {days} day(s) untill expire')