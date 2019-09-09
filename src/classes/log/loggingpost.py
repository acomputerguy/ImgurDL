import datetime

class LoggingErrors():
    def __init__(self, fileName, context):
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        filePath = "logs/" + fileName
        log_streama = open(filePath, 'a')
        if (fileName == "error.log"):
            log_streama.write(now + " - " + context + "\n")
        if (fileName == "activity.log"):
            log_streama.write(context + "|" + now + "\n")
