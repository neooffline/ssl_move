import logging
import datetime

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[logging.StreamHandler(),
              #logging.FileHandler(f'../{datetime.datetime.now().isoformat().replace(":", "-")}.log', encoding='utf-8')
              ],
)
logger = logging.getLogger(__name__)

