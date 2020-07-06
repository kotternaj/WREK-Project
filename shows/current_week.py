import datetime
from datetime import date

# determine current week to be used to name the auto-generated dirs
def current_week():
    y, m, d = date.today().year, date.today().month, date.today().day
    week_num = datetime.date(y, m, d).isocalendar()[1]
    week = str(week_num)
    return week
