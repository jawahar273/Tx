from time import sleep, strftime

from raven.utils import send_notification
from config.stage import Huey
from .models import CountdownTracker


def to_secs(mins):

    return float(mins) * 60


def to_mins(hrs):
    return float(hrs) * 60


@Huey.task(context=True)
def start_count_down_basic_case(_time, message, task=None):
    """
    task will and created and deleted after finishing
    the task can still be revoked it the task is running
    """
    # handling basic case for count down and imidetely
    countdown_sec = None

    send_notification(f"starting count down")

    if _time.find("min") is not -1:

        countdown_sec = to_secs(_time.split()[0])

    elif (_time.find("hr") or _time.find("hour")) is not -1:

        countdown_sec = to_secs(to_mins(_time.split()[0]))

    elif _time.find("sec") is not -1:

        countdown_sec = int(_time.split()[0])

    else:
        return
    # creating task id in redis
    CountdownTracker.create(id=task.id, seconds=countdown_sec)

    interval = {
        "half_interval": countdown_sec // 2,
        "quator_interval": countdown_sec // 4,
    }
    while countdown_sec >= 1:
        countdown_sec -= 1
        if interval["half_interval"] == countdown_sec:

            send_notification(f"half of the time has been over for {_time}")

        elif interval["quator_interval"] == countdown_sec:

            send_notification(f"quator of the time has been over for {_time}")

        sleep(1)
    send_notification(f"Message: {message}")

    CountdownTracker.delete(id=task.id)


def main(time, message):

    start_count_down_basic_case(time, message)


def list_of_all_task():

    return [
        {"id": task.id, "desc": task.desc, "seconds": task.seconds}
        for task in CountdownTracker.all()
    ]


def revoke_task_by_id(_id):

    try:

        result = CountdownTracker.get(id=_id)
        Huey.revoke_by_id(result)
        send_notification(f"Successfully revoked")

    except ValueError:

        send_notification(f"No id found")
