import datetime
from datetime import date

def current_week():
    y, m, d = date.today().year, date.today().month, date.today().day
    week = datetime.date(y, m, d).isocalendar()[1]
    return week
