'''
Created on 1 Dec 2021

@author: Liz-Conway
'''


class Sol():
    '''
    A Sol is a Martian day.
    This class holds the temperature, air pressure, opacity 
    and the equivalent date on earth.
    One Sol class will be created for every row of data in
    the Mars weather dataset.
    '''

    def __init__(self, earth_date, temperature, air_pressure, opacity):
        '''
        Constructor
        Parameters :
                    earth_date(date)    Equivalent date on Earth for this Sol
                    temperature(int)    Temperature for this Sol
                    air_pressure(int)    Air pressure for this Sol
                    opacity(string)     Opacity for this Sol ("Cloudy" or "Sunny")
        '''
        self.earth_date = earth_date
        self.temperature = temperature
        self.opacity = opacity
        self.air_pressure = air_pressure
