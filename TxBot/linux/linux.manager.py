from crontab import CronTab

cron = CronTab(user='jawahar')

job = cron.new(command='./TxBot/linux.manager.bash')

job.minute.every(1)

cron.write()
# cron.remove_all()
print(job.description(use_24hour_time_format=False))
