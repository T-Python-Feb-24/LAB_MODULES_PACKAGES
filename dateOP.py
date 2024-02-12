from datetime import date

def currentDate():
    today = date.today()
    return today.strftime(f"Today's Date: %d %b %Y")
