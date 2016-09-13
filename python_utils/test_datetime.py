from datetime import datetime
dt = datetime(2015, 4, 25, 13, 23, 23)
timestamp = dt.timestamp()
time = datetime.fromtimestamp(timestamp)
print(time)
cday = datetime.strptime('2016-09-04 18:19:02', '%Y-%m-%d %H:%M:%S')
print(cday)