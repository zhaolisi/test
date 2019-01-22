#coding=utf-8
import logging
import os.path
import time

class Logger(object):

    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        currenttime = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        logfilepath = os.path.dirname(os.getcwd()) + '/logs/'
        logfilename = logfilepath + currenttime +'.log'
        filehandler = logging.FileHandler(logfilename)
        filehandler.setLevel(logging.INFO)
        streamhandler = logging.StreamHandler()
        streamhandler.setLevel(logging.INFO)
        logformatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        filehandler.setFormatter(logformatter)
        streamhandler.setFormatter(logformatter)
        self.logger.addHandler(filehandler)
        self.logger.addHandler(streamhandler)

    def getlog(self):
        return self.logger

