'''
Created on 6 Dec 2021

@author: Liz-Conway
'''

from datetime import datetime
from datetime import date


class DateUtil():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.format = "%Y-%m-%d"

    def string_to_date(self, date_string):
        date_time = datetime.strptime(date_string, self.format)
        date_date = datetime.date(date_time)
        return date_date
