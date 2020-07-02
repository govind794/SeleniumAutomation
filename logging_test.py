import logging

logging.basicConfig(filename='/Users/govind794/Documents/GitHub/SeleniumAutomation/logs/home.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%d/%m/%y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
