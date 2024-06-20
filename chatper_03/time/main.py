import time

# print(time.ctime(100000000))

# epoch time in seconds relying on system clock
# print(time.time())

# now time
# print(time.ctime(time.time()))

# formatting time to a readable string
# time_object = time.localtime()
# print(time_object)
# print(time.strftime("%a %m %Y", time_object))

# parsing a time string
# time_string = '20 April, 2020'
# time_obj = time.strptime(time_string, '%d %B, %Y')
# print(time_obj)

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# print(time.asctime(time_tuple))   # readable string from time_tuple

# (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
print(time.mktime(time_tuple))   # seconds since epoch
