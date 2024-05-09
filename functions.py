from log import logConfiguration

import traceback
import os
import logging.config
import datetime

infoLog = logging.getLogger('infoLog')

def checkIsDigit(input_str):
    try:
        infoLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.strip().isdigit()
    
    except Exception as error:
        infoLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        infoLog.error(traceback.format_exc())

def mkdir():
    infoLog = logging.getLogger('infoLog')
    path = "logs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            #infoLog.info(f"Path \"{path}\" wasn't found. New folder named \"{path}\" was created")
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            print(traceback.format_exc())
            #infoLog.error(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            #infoLog.error(traceback.format_exc())

def checkYNInput(stringInput):
    return stringInput.lower() == 'y' or stringInput.lower() == 'n'