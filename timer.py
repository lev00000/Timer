import time



set_time=int(input("Set your time:"))
print("countdown is started")
while set_time>0:
    print(set_time)
    time.sleep(1)
    set_time-=1
else:
    print("Time is up")

