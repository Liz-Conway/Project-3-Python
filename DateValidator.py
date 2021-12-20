'''
Created on 5 Dec 2021

@author: Liz-Conway
'''

from datetime import datetime
from datetime import date


class DateValidator():
    '''
    Responsible for ensuring that any dates are in a valid format
    and fall within the specified date range
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.format = "%Y-%m-%d"
        self.min_date = date(2012, 8, 15)
        self.max_date = date(2018, 2, 27)

    def validateDate(self, date_string):
        '''
        Validates that the date is both in valid format 
        and falls within acceptable date range
        Parameters : date_string(string) Date to check for validity
        '''
        valid = False

        validFormat = self.validDateFormat(date_string)

        validRange = False
        if validFormat is True:
            validRange = self.validDateRange(date_string)

        # Check date is both in correct format
        # and falls within the acceptable date range
        valid = validFormat and validRange

        return valid

    def validDateFormat(self, date_string):
        '''
        Validates a date as conforming to the correct format
        Parameters : date_string(string) Date to check for valid format
        '''
        validated = True

        try:
            # https://stackabuse.com/how-to-format-dates-in-python/
            datetime.strptime(date_string, self.format)
        except ValueError:
            validated = False

        return validated

    def validDateRange(self, date_string):
        '''
        Ensures the date falls within the acceptable date range
        as specified by the min_date and max_date
        Parameters : date_string(string) Date to check if in acceptable range
        '''
        validRange = False

        # https://stackabuse.com/how-to-format-dates-in-python/
        date_time = datetime.strptime(date_string, self.format)
        date_date = datetime.date(date_time)

        if date_date >= self.min_date and date_date <= self.max_date:
            # Date is within acceptable range
            validRange = True

        return validRange
