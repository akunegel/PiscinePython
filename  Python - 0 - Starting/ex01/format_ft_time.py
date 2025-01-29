import datetime
import calendar

now = datetime.datetime.now()
time = now - datetime.datetime(1970, 1, 1)
seconds = time.total_seconds()
print("Seconds since January 1, 1970:", f'{seconds:,}', "or", format(time.total_seconds(), ".2e"), "in scientific notation")
month = calendar.month_name[now.month]
print(month[:3], now.day, now.year)