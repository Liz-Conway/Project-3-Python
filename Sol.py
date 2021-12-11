'''
Created on 1 Dec 2021

@author: Liz-Conway
'''

class Sol():
    '''
    classdocs
    '''


    def __init__(self, earth_date, temperature, air_pressure, opacity):
        '''
        Constructor
        '''
        self.earth_date = earth_date
        self.temperature = temperature
        self.opacity = opacity
        self.air_pressure = air_pressure
        
    def __eq__(self, other):
        return self.earth_date == other.earth_date and \
            self.temperature == other.temperature and \
            self.opacity == other.opacity and \
            self.air_pressure == other.air_pressure
            
    def __str__(self):
        me = "Date :  " + str(self.earth_date)
        me += "  Temp: " + str(self.temperature)
        me += "  Opacity:  " + str(self.opacity)
        me += "  Pressure:  " + str(self.air_pressure)
        
        return me