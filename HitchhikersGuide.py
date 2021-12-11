'''
Created on 7 Dec 2021

@author: Liz-Conway
'''
from LoadData import LoadData
from DateValidator import DateValidator
from WeatherActivity import WeatherActivity

def main():
    '''
    Launch point for the Hitchhiker's Guide to the Red Planet
    '''
    print("Loading weather_data!!!")
    load_data = LoadData('../mars-weather.csv')
    load_data.load()
    print("Data loaded successfully!")
    #weather_data = load_data.weather
    # Loop to get valid input from the user
    while True:
        print("Please enter a date in the format yyyy-mm-dd  E.G. 2015-03-24")
        print("Valid dates are between 2012-08-15 and 2018-02-27\n")
        search_date = input("What date are you arriving on Mars?\n")
        
        date_validator = DateValidator()
        valid_date = date_validator.validateDate(search_date)
        
        if not valid_date :
            # If the date is not valid
            # Skip the rest of the loop
            # and continue at the start of the while loop again
            # asking for the date
            break
    
    # Congratulations you have valid data!!
    # The rest of the program starts here :
    # Retrieve the weather for the entered dates
    weather_day = load_data.search_for_day(search_date)
    
    # Get the median temperature for the entire set of data
    median_temperature = load_data.get_median_temperature()
    # print(f"Median Temp:  {median_temperature}")
    
    # Get the median air pressure for the entire set of data
    median_air_pressure = load_data.get_median_air_pressure()
    # print(f"Median Pressure:  {median_air_pressure}")
    
    # WeatherActivity uses the median temperature and air pressure
    # to determine whether a particular day's value is "High" or "Low"
    weather_activity = WeatherActivity(median_temperature, median_air_pressure)
    # Retrieve the activity for the entered date
    activity = weather_activity.decideWeatherActivity(weather_day)
    
    #Show the user the selected activity for their arrival day
    print("Congratulations the following activity has been specially chosen for you\n")
    print(f"    {activity}\n")
    

print("~"*40)
print("  Hitchhiker's Guide to the Red Planet")
print("~"*40)
main()


