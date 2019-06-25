
from time import sleep, strftime

from plyer import notification

from config.stage import Huey


def to_secs(mins):
    
    return float(mins) * 60


def to_mins(hrs):
    return float(hrs) * 60


@Huey.task()
def start_count_down_basic_case(_time):
    # handling basic case for count down and imidetely
    countdown_sec = None
    notification.notify(f'starting count down')
    if _time.find('min') is not -1:
        countdown_sec = to_secs(_time.split()[0])
    elif (_time.find('hr') or _time.find('hour')) is not -1:
        countdown_sec = to_secs(
            to_mins(_time.split()[0]) 
        )
    elif _time.find('sec') is not -1:
        countdown_sec = int(_time.split()[0])
    else:
        return 
    interval = {
        'half_interval': countdown_sec // 2,
        'quator_interval': countdown_sec // 4
    }
    while countdown_sec >= 1:
        countdown_sec -= 1
        if interval['half_interval'] == countdown_sec:
            notification.notify(f'half of the time has been over for {_time}')
        elif interval['quator_interval' ] == countdown_sec:
            notification.notify(f'quator of the time has been over for {_time}')

        sleep(1)
    notification.notify(f'count down done')         


def main(time):
    start_count_down_basic_case(time)
