import logging
logging.basicConfig(filename='app.log',
filemode='a',
format='%(name)s - %(levelname)s - %(message)s')
logging.error('This is an error message')

