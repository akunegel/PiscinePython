from datetime import datetime

s = 0

t = datetime.now()
s += (t.year - 1970) * 31556952
s += t.month * 2628288
s += t.day * 86400
s += t.hour * 3600
s += t.minute * 60
s += t.second


print("Seconds since January 1 1970:", s, "or", "{:e}".format(s), "in scientific notation Oct 21 2022")
print(t.strftime("%B"), t.day, t.year)