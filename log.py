import logging
import logging.config
import os
import traceback

logConfiguration = {
    'version': 1,
    'loggers': {
        'debugLog': {
            'level': 'DEBUG',
            'handlers': ['debugHandler']
        },
        'errorLog': {
            'level': 'ERROR',
            'handlers': ['errorHandler']
        },
        'infoLog': {
            'level': 'INFO',
            'handlers': ['infoHandler']
        },
    },
    'handlers': {
        'debugHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'DEBUG',
            'formatter': 'completeFormat'
        },
        'errorHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'ERROR',
            'formatter' : 'logFormat'
        },
        'infoHandler' : {
            'class': 'logging.FileHandler',
            'filename': 'logs/systemLogs.txt',
            'level': 'INFO',
            'formatter' : 'logFormat'
        },
    },
    'formatters': {
        'logFormat': {
            'format' : "%(asctime)s - %(levelname)s - %(message)s"
        },
        'completeFormat': {
            'format' : "%(asctime)s - %(levelname)s - %(message)s - %(pathname)s - %(module)s - %(lineno)d - %(process)d - %(thread)d"
        },
    }
}

def mkdir():
    path = "logs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            infoLog.info(f"Path \"{path}\" wasn't found. New folder named \"{path}\" was created")
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            infoLog.error(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            infoLog.error(traceback.format_exc())

logging.config.dictConfig(logConfiguration)
infoLog = logging.getLogger('infoLog')