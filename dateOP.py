import datetime 
def current_date():
    '''function to print the current date'''
    date=datetime.datetime.now()
    print("the current date: ",date.strftime("%y /%m /%d"))

