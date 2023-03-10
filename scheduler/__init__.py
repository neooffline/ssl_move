from flask import Flask, logging as flog
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import logging


format = '%(asctime)s %(levelname)s: %(message)s'

class Config:
    SCHEDULER_API_ENABLED = True


app = Flask(__name__)
app.config.from_object(Config())
flog.default_handler.setFormatter(logging.Formatter(format))
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
