import datetime

d, m, y = [int(x) for x in input().strip(" ").split(" ")]
end_date = datetime.datetime(y-543, m, d) + datetime.timedelta(days=15)
print(str(end_date.day) + "/" + str(end_date.month) + "/" + str(end_date.year+543))
