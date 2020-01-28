from datetime import datetime, timedelta

#Return (int) seconds since 1st january 1970 (Known as Posix Time, Unix epoch, Unix Timestamp)
def getUnixTimeStamp():
    now = datetime.now()
    return int(datetime.timestamp(now))

#Return (float) seconds since 1st january 1970 (Known as Posix Time, Unix epoch, Unix Timestamp)
def getUnixTimeStampFloat():
    now = datetime.now()
    return datetime.timestamp(now)

def getTimeStamp(format=None):
    if(format==None):
        return datetime.now().strftime("%Y%m%d%H%M%S.%f")
    else:
        return datetime.now().strftime(format)

#Return 2020-01-12 19:11:39.239338
def getDateTime(): 
    return datetime.now()

# Input "YYYYMMDDHHMMSS.XYZ"
# Return ("DD/MM/AAAA", "HH:MM:SS")
def getDateTimeFromFilename(filename):
    splitUp = filename.split(".")
    dt = datetime.strptime(splitUp[0], "%Y%m%d%H%M%S")
    date = dt.strftime("%d/%m/%Y")
    time = dt.strftime("%H:%M:%S")
    return date, time

# Input "YYYYMMDDHHMMSS"
# Return ("DD/MM/AAAA", "HH:MM:SS")
def getDateTimeFromString(str):
    dt = datetime.strptime(str, "%Y%m%d%H%M%S")
    date = dt.strftime("%d/%m/%Y")
    time = dt.strftime("%H:%M:%S")
    return date, time

#Return 2020-01-12
def getDate(): 
    return datetime.now().date()

#Return 19:11:39
def getTime(): 
    return datetime.now().strftime("%X")

#Return 19:11:39.239338
def getTimeMs(): 
    return datetime.now().time()

#Return day of yesterday, based on time delta
def getYesterdayTimeStamp(format=None):
    if(format==None):
        return datetime.strftime(datetime.now() - timedelta(1), "%Y%m%d")
    else:
        return datetime.strftime(datetime.now() - timedelta(1), format)