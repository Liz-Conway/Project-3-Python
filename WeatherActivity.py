'''
Created on 1 Dec 2021

@author: Liz-Conway
'''
from colorama import init, Fore, Back
from colorama.ansi import Style


class WeatherActivity():
    '''
    classdocs
    '''

    def __init__(self, avg_temp, avg_pressure):
        '''
        Constructor
        Parameters :
                    avg_temp(int)    Average temperature for the dataset
                    avg_pressure(int)    Average air pressure for the dataset
        '''
        self.average_temperature = avg_temp
        self.average_air_pressure = avg_pressure

    def decideWeatherActivity(self, sol):
        '''
        Calculates the holiday activity applicable for the passed in Sol.
        This is done by comparing the temparature and air pressure with the
        median temperature and air pressure to determine if they are
        "High" or "Low".  Also the opacity is checked to see if it is
        "Cloudy" or "Sunny".
        Depending on what these weather conditions are different holiday
        activities are chosen.
        Parameters : sol(Sol)    The Sol whose activity this method will check
        Return :    activity(string)    A string denoting the chosen activity
        '''
        activity = "Do nothing"
        # https://stackabuse.com/how-to-format-dates-in-python/
        activity_date = sol.earth_date.strftime("%A, %d %b %Y")
        # Add padding to end of the activity date
        # This will align the output when printed to the screen
        # https://www.delftstack.com/howto/python/python-pad-string-with-spaces
        activity_date = activity_date.ljust(22)

        if sol.temperature == "NaN":
            # Some days returned erroneous data (NaN)
            # thus cannot return an activity
            return f"Planet closed on :  {activity_date}"

        if sol.temperature > self.average_temperature:  # High Temperature
            if sol.opacity == "Sunny":
                # High Temp & Sunny
                if sol.air_pressure > self.average_air_pressure:
                    # High Temp, Sunny, High pressure
                    activity = "Paragliding"
                else:
                    # High Temp, Sunny, Low pressure
                    activity = "Sunbathing"
            else:
                # High Temp, Cloudy
                if sol.air_pressure > self.average_air_pressure:
                    # High Temp, Cloudy, High pressure
                    activity = "Blind Date"
                else:
                    # High Temp, Cloudy, Low pressure
                    activity = "Happy Hour"
        else:
            # Low Temperature
            if sol.opacity == "Sunny":
                # Low Temp, Sunny
                if sol.air_pressure > self.average_air_pressure:
                    # Low Temp, Sunny & High pressure
                    activity = "Star Gazing"
                else:
                    # Low Temp, Sunny, Low pressure
                    activity = "Volleyball"
            else:
                # Low Temp, Cloudy
                if sol.air_pressure > self.average_air_pressure:
                    # Low Temp, Cloudy, High pressure
                    activity = "Ski at poles"
                else:
                    # Low Temp, Cloudy, Low pressure
                    activity = "Play Sardines"

        # Add padding to end of the activity
        # This will align the output when printed to the screen
        # https://www.delftstack.com/howto/python/python-pad-string-with-spaces
        activity = activity.ljust(13)

        return f"{activity_date} :  " + Fore.RED + f"{activity}" + Fore.RESET
