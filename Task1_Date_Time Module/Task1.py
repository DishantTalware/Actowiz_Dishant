
# Write a Python script to display the various Date Time formats 

'''
    a) Current date and time
    b) Current year
    c) Month of year
    c
'''
#-----------------------------------------------------------------------------------------

from datetime import datetime

# a) Current date and time 

current_date_time = datetime.now()
print(f'curret Date & Time = {current_date_time}')



# b) Current year

current_year = datetime.today().strftime("%Y")
print(current_year)



# c) Month of year

current_month = datetime.today().strftime("%B")
print(current_month)



# d) Week number of the year

current_week = datetime.today().strftime("%W")
print(current_week)



# e) Weekday of the week

current_week = datetime.today().strftime("%w")
print(current_week)



# f) Day of year

current_day = datetime.today().strftime("%j")
print(current_day)



# g) Day of the month

current_date = datetime.today().strftime("%d")
print(current_day)



# h) Day of week 

current_day_of_week = datetime.today().strftime("%A")
print(current_day_of_week)



