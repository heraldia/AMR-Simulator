import sys
import traceback
import logging
import time
import requests
import datetime
import os

def get_time():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H%M%S')

log_level = int(os.environ.get('LOG_LEVEL', 3))

#                    0              1              2            3
loggingLevel = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]
LOGPREFIX = "[AGV] " 

# logging set up
logger = logging.getLogger(__name__)
logger.setLevel(loggingLevel[log_level])  # the level should be the lowest level set in handlers

log_format = logging.Formatter( '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_format)

stream_handler.setLevel(loggingLevel[log_level])

logger.addHandler(stream_handler)
