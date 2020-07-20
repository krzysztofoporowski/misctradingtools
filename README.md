# misctradingtools
Tools used for excercises related to trading scripts

Functions
get_prev_workday_datestring():
    '''
    Function checks the current day of week and returns the date of previous
    work day, e.g. on Wednesday it is going to return the date of Tuesday,
    on Saturday, Sunday and Monday it is going to return the date of Friday.
    Return:
    -------
    date_string - string representing the previous working day date, format
                  yyyy-mm-dd
    '''
