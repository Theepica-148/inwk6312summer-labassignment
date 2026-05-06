import logging
logging.basicConfig(format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger('example_logger')
logger.warning('This is a warning')
