from log import infoLog
import traceback

def checkIsDigit(input_str):
    try:
        infoLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.strip().isdigit()
    
    except Exception as error:
        infoLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        infoLog.error(traceback.format_exc())