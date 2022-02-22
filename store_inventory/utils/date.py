import datetime


def clean_date(date_str):
    split_date = date_str.split("/")

    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    return datetime.date(year, month, day)


def generate_date():
    pass

