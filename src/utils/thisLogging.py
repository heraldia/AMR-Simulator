import logging
import logging.handlers
#from opencensus.ext.azure.log_exporter import AzureLogHandler
import os
import datetime
import time
import sys

level = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG][1]


def get_time():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%dT%H%M%S')


def get_logger(cur_name):
    # fh = logging.handlers.RotatingFileHandler(f'{get_time()}_debug.log')
    # fh.setLevel(logging.DEBUG)
    # fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    fh2 = logging.handlers.RotatingFileHandler(f'consumer-{get_time()}.log')
    fh2.setLevel(logging.DEBUG)
    fh2.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'))

    # er = logging.handlers.RotatingFileHandler(f'{get_time()}_error.log')
    # er.setLevel(logging.WARNING)
    # er.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter(
        '%(name)s - %(levelname)s - %(lineno)d - %(message)s'))

    logger = logging.getLogger(cur_name)

    # alternatively:
    # logger.setLevel(min([fh.level, fh2.level, ch.level, er.level])

    # logger.addHandler(fh)
    logger.addHandler(fh2)
    logger.addHandler(ch)
    # logger.addHandler(er)
    logger.setLevel(logging.DEBUG)

    return logger


def get_global_logger(cur_name, generate_local_log=0):

    # GENERATE_LOCAL_LOG: 0-prod; 1-dev; 2-qa; 4- generate_local_log

    if generate_local_log == 4:
        logger = get_logger(cur_name)  # generate a log file on local macbook
    else:
        logger = logging.getLogger(cur_name)

        if generate_local_log in {0, 2}:
            logger_level = logging.WARNING
            #logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=cc006dc5-e616-4195-b59f-5bbf3ea0dc1b'))

            myHandler = logging.StreamHandler(sys.stdout)
            # myHandler.setLevel(logger_level)
            myHandler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'))
            logger.addHandler(myHandler)

            logger.setLevel(logger_level)

        else:  # dev
            logger_level = logging.DEBUG
            myHandler = logging.StreamHandler(sys.stdout)
            # myHandler.setLevel(logger_level)
            myHandler.setFormatter(logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s'))
            logger.addHandler(myHandler)
            logger.setLevel(logger_level)

    return logger
