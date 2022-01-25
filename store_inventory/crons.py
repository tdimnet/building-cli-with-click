from crontab import CronTab

cron = CronTab(user=True)
job = cron.new(command='python app.py product update')
job.minute.every(1)

cron.write()

