'''
Author: Krzysztof Oporowski
krzysztof.oporowski@gmail.com

Set of miscalenious tools used for trading operations
'''

from datetime import date, timedelta
from pathlib import Path
import matplotlib.pyplot as plt

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

def get_date_from_past(past=7):
    '''
    Function returns date older than today minus past

    Parameters:
    -----------
    past - intiger, number of days used to calculate past date

    Returns:
    --------
    date in the Pandas DateTime format
    '''
    today = date.today()
    past_date = today - timedelta(days=past)
    return past_date

def plot_ichimoku(data, stock_name, buy_data, sell_data):
    '''
    Function to plot stocks with Ichimoku settings
    Parameters:
    -----------
    data - pandas DataFrame with columns: close, tenkan_sen, senkou_span_a,
           senkou_span_b, kijun_sen, chikou_span
    stock_name - name of the stock
    buy_data - subset of data where signal is equal 1
    sell_data - subset of data where signal is equal -1
                Prepare that data:
                    buy = data[data.signal == 1]
                    sell = data[data.signal == -1]
    '''
    axis1 = data.close.plot(figsize=(15, 10), title=stock_name, color='black',
                            linewidth=1, label='close')
    axis1 = data.tenkan_sen.plot(figsize=(15, 10), color='pink',
                                 linewidth=1, label='tenkan sen')
    axis1 = data.senkou_span_a.plot(figsize=(15, 10), color='lightgreen',
                                    linewidth=1)
    axis1 = data.senkou_span_b.plot(figsize=(15, 10), color='black',
                                    linewidth=1)
    axis1 = data.kijun_sen.plot(figsize=(15, 10), color='blue',
                                linewidth=1, label='kijun_sen')
    axis1 = data.chikou_span.plot(figsize=(15, 10), color='lightgreen',
                                  linewidth=1, label='chikou span')
    axis1.fill_between(data.index, data.senkou_span_a, data.senkou_span_b,
                       where=data.senkou_span_a >= data.senkou_span_b,
                       color='lightgreen')
    axis1.fill_between(data.index, data.senkou_span_a, data.senkou_span_b,
                       where=data.senkou_span_a < data.senkou_span_b,
                       color='lightcoral')
    axis1.scatter(x=buy_data.index, y=buy_data.open, marker="^", c='green')
    axis1.scatter(x=sell_data.index, y=sell_data.open, marker="v", c='red')
    plt.legend()
    plt.show()

def return_data_path():
    '''
        Function to be used with programs working on the polish stock exchnge
        data downloaded from the bossa.pl website.
        There is an assumption, that the data is stored in the ~/python/data
        folder.

        Return:
        -------
            data_path - string contating path to the data folder with the
                        python folder as a parent
    '''
    path = Path()
    current_path = path.cwd()
    current_parent = current_path.parents[0]
    data_path = current_parent.joinpath('data')
    return data_path

if __name__ == '__main__':
    print('This is a module, please, import it.')
