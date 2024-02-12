
## Create a new module and name it "dateOP.py" ,  
# dateOP has the following:
# - A function that when called prints the current date.

from datetime import date 

def current_date():
    dates = date.today()
    return dates