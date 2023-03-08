from datetime import datetime


def expires_days(expires_):
    return (expires_ - datetime.now()).days