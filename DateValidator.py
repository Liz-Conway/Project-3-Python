'''
Created on 5 Dec 2021

@author: Liz-Conway
'''

from datetime import datetime
from datetime import date


class DateValidator():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.format = "%Y-%m-%d"
        self.min_date = date(2012, 8, 15)
        self.max_date = date(2018, 2, 27)

    def validateDate(self, date_string):
        valid = False

        validFormat = self.validDateFormat(date_string)

        validRange = False
        if validFormat is True:
            validRange = self.validDateRange(date_string)

        valid = validFormat and validRange

        return valid

    def validDateFormat(self, date_string):
        validated = True

        try:
            datetime.strptime(date_string, self.format)
        except ValueError:
            validated = False

        return validated

    def validDateRange(self, date_string):
        validRange = False

        date_time = datetime.strptime(date_string, self.format)
        date_date = datetime.date(date_time)

        if date_date >= self.min_date and date_date <= self.max_date:
            validRange = True

        return validRange
