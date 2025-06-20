import time
import json

class Timer():
    def __init__(self):
        self.load_settings()
        self.current_state = 'WORK'


    def save_settings(self, dict):
        with open('settings.json', 'w') as f:
            json.dump(dict, f)


    def load_settings(self):
        try:
            with open ('settings.json', 'r') as f:
                settings = f.read()
        except:
            self.settings = {
                'work_time': 25,
                'break_time': 5,
                'long_break_time': 15,
                'auto_work_starting': False,
                'auto_break_starting': True
            }
            self.save_settings(self.settings)


    def change_state(self):
        flag = True
        states = ['work', 'break', 'long break']
        while flag:
            if a := input('Type one of this statuses: work, break, long break: ') in states:
                flag = False
                match a:
                    case 'work':
                        self.current_state = 'WORK'
                    case 'break':
                        self.current_state = 'BREAK'
                    case 'long break':
                        self.current_state = 'LONGBREAK'
            else:
                print("I don't understood you.")


    def control(self):
        flag =True
        while flag:
            command = input('Type a command or "help" for information: ')
            match command:
                case 'start':
                    self.start_timer(self.work_time, self.break_time, self.long_brre)
                case 'settings':
                    self.update_settings()
                case 'change':
                    self.change_state()
                case 'stats':
                    self.check_stats()
                case 'exit': exit()
                case 'help':
                    print("""
Use this:
    -start: start timer
    -change: change state of timer
    -stats: statistics of using pomodoro timer
    -settings: change settings
    -exit: exit from timer
    """)
                case _:
                    print("""
Unknown command. Use this:
    -start: start timer
    -change: change state of timer
    -stats: statistics of using pomodoro timer
    -settings: change settings
    -exit: exit from timer
    """)
        


if __name__ == '__main__':
    timer = Timer()
    timer.control()