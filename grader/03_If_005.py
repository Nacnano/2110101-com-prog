import math
import datetime

bd, bm, by, d, m, y = [int(e) for e in input().split()]
end_date = datetime.datetime(y-543, m, d) + datetime.timedelta(days=15)
print(str(end_date.day) + "/" + str(end_date.month) + "/" + str(end_date.year+543))

t = (bd, bm, by-543, d, m, y-543)

print("{} {:.2f} {:.2f} {:.2f}".format(t, math.sin(2*t*math.pi/23), math.sin(2*t*math.pi/28), math.sin(2*t*math.pi/33)))
