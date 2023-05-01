from flask import Flask
from datetime import datetime
import pytz
from scheduler import scheduler, CronTrigger


def add_job(func_, params_: list, id_: str):
    scheduler.add_job(id=id_, 
                      func=func_, 
                      trigger=CronTrigger.from_crontab('*/1 * * * *'), 
                      args=[params_], 
                      next_run_time=datetime.now(pytz.timezone('Europe/Moscow')))