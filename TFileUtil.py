# GENERAL
STATUS_OK = 0
# STATUS DIRECTORY
IS_WRITABLE = 1
IS_DIRECTORY = 2
IS_FILE = 3    
# ERRORS DIRECTORY
DIRECTORY_DO_NOT_EXIST = -1   
IS_NOT_WRITABLE = -2

def isDirectory(self, directory):
    if os.path.exists(directory):
        if os.path.isfile(directory):
            return Timelapse.IS_FILE
        else:
            return Timelapse.IS_DIRECTORY
    else:
        return Timelapse.DIRECTORY_DO_NOT_EXIST

def isWritable(self, directory):
    if(os.access(directory, os.X_OK | os.W_OK) == True):
        return Timelapse.IS_WRITABLE
    else:
        return Timelapse.IS_NOT_WRITABLE