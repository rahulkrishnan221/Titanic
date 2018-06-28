import datetime as dt
import time as tm
tm.time()
dtnow = dt.datetime.fromtimestamp(tm.time())
delta = dt.timedelta(days = 100)
today = dt.date.today()
print(today - delta)