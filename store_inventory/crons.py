from crontab import CronTab
import os


cron = CronTab(user=True)

def add_product_crons():
    job = cron.new(command="/usr/local/bin/python /app/app.py product update >> /var/log/cron.log 2>&1")
    job.minute.every(1)
    cron.write()
    job.enable()


def shipped_cron():
    job = cron.new(command="/usr/local/bin/python /app/app.py product update_product >> /var/log/cron.log 2>&1")
    job.minute.every(1)
    cron.write()
    job.enable()


def list_crons():
    for job in cron:
        print(job)

