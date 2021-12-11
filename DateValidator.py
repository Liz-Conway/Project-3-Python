'''
Created on 5 Dec 2021

@author: Liz-Conway
'''

from datetime import datetime

class DateValidator():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.format = "%Y-%m-%d"

    def validateDate(self, date_string):
        valid = False
        
        validFormat = self.validDateFormat(date_string)
        
        valid = validFormat
        
        return valid
        
    def validDateFormat(self, date_string):
        validated = True

        try:
            datetime.strptime(date_string, self.format)
        except ValueError:
            validated = False
            
        return validated
            