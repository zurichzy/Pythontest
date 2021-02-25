



import  time

# print(time.asctime())
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y-%m-%d"),time.localtime())

#获取两天前的时间
now_timestamp=time.time()
two_day_before=now_timestamp-60*60*24*2
