'''
Created on 1 Dec 2021

@author: Liz-Conway
'''

class WeatherActivity():
    '''
    classdocs
    '''

    def __init__(self, avg_temp, avg_pressure):
        '''
        Constructor
        '''
        self.average_temperature = avg_temp
        self.average_air_pressure = avg_pressure
        
    def decideWeatherActivity(self, sol):
        activity = "Do nothing"
        # https://stackabuse.com/how-to-format-dates-in-python/
        activity_date = sol.earth_date.strftime("%A, %d %b %Y")
        
        if sol.temperature == "NaN" :
            return f"Resort closed on :  {activity_date}"
        
        if sol.temperature > self.average_temperature : # High Temperature
            if sol.opacity == "Sunny" :     #High Temp & Sunny
                if sol.air_pressure > self.average_air_pressure : #High Temp, Sunny, High pressure
                    activity = "Paragliding"
                else:                                       # High Temp, Sunny, Low pressure
                    activity = "Sunbathing"
            else :                                  #High Temp, Cloudy
                if sol.air_pressure > self.average_air_pressure : #High Temp, Cloudy, High pressure
                    activity = "Blind Date"
                else :                          #High Temp, Cloudy, Low pressure
                    activity = "Happy Hour"
        else :                                          # Low Temperature
            if sol.opacity == "Sunny" :     #Low Temp, Sunny
                if sol.air_pressure > self.average_air_pressure : #Low Temp, Sunny & High pressure
                    activity = "Star Gazing"
                else:                                 # Low Temp, Sunny, Low pressure
                    activity = "Volleyball"
            else :                                  #Low Temp, Cloudy
                if sol.air_pressure > self.average_air_pressure : #Low Temp, Cloudy, High pressure
                    activity = "Ski at poles"
                else :                          #Low Temp, Cloudy, Low pressure
                    activity = "Play Sardines"
            
            
        return f"{activity_date} :  {activity}"
    

    
