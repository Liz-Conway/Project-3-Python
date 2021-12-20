'''
Created on 6 Dec 2021

@author: Liz-Conway
'''

from datetime import datetime
from datetime import date


class DateUtil():
    '''
    Utility class to deal with date functionality
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.format = "%Y-%m-%d"

    def string_to_date(self, date_string):
        '''
        Takes a textual description of a date and returns a date object
        Parameters : date_string(string)    Textual date to convert to a date
        '''
        # https://stackabuse.com/how-to-format-dates-in-python/
        date_time = datetime.strptime(date_string, self.format)
        date_date = datetime.date(date_time)
        return date_date
