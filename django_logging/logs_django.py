import logging 

# Defining a Logger
logger = logging.getLogger(__name__)
# set level of logger to debug
logger.setLevel(logging.DEBUG)
# formatting logger
formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(message)s')
# file handler
file_handler = logging.FileHandler('test.log')
# set level at file handler to be ERROR
file_handler.setLevel(logging.ERROR)
# Applyling Formatter
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# This is a basic config with level , format , file_handler also defined 
# logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s- %(message)s',filename="test.log")

# logger with info level 

logger.info('This is info level.')


# logger with error level 

def div(x,y):
    return x / y
try:
    div(1,0)
except:
    logger.error('Tried to Divide by zero')
    pass    

# logger with exception level  (Comment + actual error thrown by python terminAL)

def div(x,y):
    return x / y
try:
    div(1,0)
except:
    logger.exception('Include exception')
    pass    

# logger with debug level

def add(x,y):
    return x+y

logger.debug('Addition working fine ')
    







