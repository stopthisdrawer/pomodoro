import time

work_time = 1
break_time = 1
long_break_time = 1

def start_timer(wt, bt, lbt):
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


def settings():
    pass


def stats():
    pass


def control():
    flag =True
    while flag:
        command = input('Type a command: ')
        match command:
            case 'start':
                start_timer(work_time, break_time, )
            case 'settings':
                settings()
            case 'stats':
                stats()
            case 'exit': exit()
            case _:
                print("""
Unknown command. Use this:
-start: start timer
-stats: statistics of using pomodoro timer
-settings: change settings
-exit: exit from timer
""")
        


if __name__ == '__main__':
    control()