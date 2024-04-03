import datetime
def get_days_from_today(date):

    transform = datetime.datetime.strptime(date,'%Y-%m-%d').date()
    today = datetime.date.today()
    if transform<today:
        res=today - transform
    else:
        res = transform-today
    return res.days

print(get_days_from_today('2024-10-09'))





