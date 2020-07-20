'''
Author: Krzysztof Oporowski
krzysztof.oporowski@gmail.com

Set of miscalenious tools used for trading operations
'''

from datetime import date, timedelta

def get_prev_workday_datestring():
    '''
    Function checks the current day of week and returns the date of previous
    work day, e.g. on Wednesday it is going to return the date of Tuesday,
    on Saturday, Sunday and Monday it is going to return the date of Friday.
    Return:
    -------
    date_string - string representing the previous working day date, format
                  yyyy-mm-dd
    '''
    day_of_week = date.today().weekday()
    if day_of_week == 0:
        # 0 - Monday
        date_string = str(date.today() - timedelta(days=3))
    elif day_of_week == 6:
        # 6 - Sunday
        date_string = str(date.today() - timedelta(days=2))
    else:
        # for any other day of week
        date_string = str(date.today() - timedelta(days=1))
    return date_string

if __name__ == '__main__':
    print('This is a module, please, import it.')
