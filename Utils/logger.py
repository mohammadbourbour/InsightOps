# utils/logger.py

import logging

class Logger:
    def __init__(self):
        # Setting up a logger with the name 'InsightOpsLogger'
        self.logger = logging.getLogger('InsightOpsLogger')
        self.logger.setLevel(logging.DEBUG)  # Setting the logging level to DEBUG
        ch = logging.StreamHandler()  # Creating a stream handler to print logs
        self.logger.addHandler(ch)  # Adding the handler to the logger

    def log(self, message):
        # Method to log a general message
        self.logger.info(message)

    def log_error(self, message):
        # Method to log an error message
        self.logger.error(message)
