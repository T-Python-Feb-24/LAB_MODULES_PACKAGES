import datetime

def current_date():
    now = datetime.datetime.now()
    print("Current date is ",now.strftime("%d/%m/%Y, %H:%M:%S"))