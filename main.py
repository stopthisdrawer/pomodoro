import time

work_time = 1*60
break_time = 1*60

def start_timer(wt, bt):
    while wt != 0:
        print(f'{wt//60}:{wt%60}')
        wt-=1
        time.sleep(1)
    print('Time to break')
    while bt != 0:
        print(f'{bt//60}:{bt%60}')
        bt-=1
        time.sleep(1)
    print('Time to work!')


a = input()
if a=='start':
    start_timer(work_time, break_time)