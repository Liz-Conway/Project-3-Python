'''
Created on 1 Dec 2021

@author: Liz-Conway
'''

class WeatherActivity():
    '''
    classdocs
    '''
    #average_temperature = 0
    #average_opacity = 0
    #average_wind_speed = 0


    def __init__(self, avg_temp, avg_opacity, avg_wind):
        '''
        Constructor
        '''
        self.average_temperature = avg_temp
        self.average_opacity = avg_opacity
        self.average_wind_speed = avg_wind
        
    def decideWeatherActivity(self, sol):
        activity = "Do nothing"
        
        print(sol)
        print(sol.temperature)
        print(self.average_temperature)
        
        if sol.temperature > self.average_temperature : # High Temperature
            activity = "Paragliding"
        else :                                          # Low Temperature
            activity = "Play Sardines"
            
            
            
        return activity
    
    
    