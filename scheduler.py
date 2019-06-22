import schedule
import time

from config.stage import db

while True:
    schedule.run_pending()
    time.sleep(1)