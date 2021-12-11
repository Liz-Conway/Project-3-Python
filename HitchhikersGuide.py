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
    load_data = LoadData('mars-weather.csv')
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
            continue
        
        stay_days = input("How many days will you be staying (positive integers only)?\n")
        
        # https://www.pythonpool.com/python-check-if-string-is-integer/
        # isdigit() Only allows positive integers
        valid_days = stay_days.isdigit()
        
        # If we get here the date is valid, so we only need to worry about the stay_days
        if valid_days :   # Days are valid
            # If the days entered are valid then
            # break out of this while loop and continue running the rest of the program
            # If the days entered is not a positive integer then
            # the while loop will keep looping until a valid date and days are entered
            break
    
    # Congratulations you have valid data!!
    # The rest of the program starts here :
    # Retrieve the weather for the entered dates
    weather_days = load_data.search_for_days(search_date, stay_days)
    
    # Get the median temperature for the entire set of data
    median_temperature = load_data.get_median_temperature()
    
    # Get the median air pressure for the entire set of data
    median_air_pressure = load_data.get_median_air_pressure()
    
    # WeatherActivity uses the median temperature and air pressure
    # to determine whether a particular day's value is "High" or "Low"
    weather_activity = WeatherActivity(median_temperature, median_air_pressure)
    
    # Retrieve the activities for the entered date and stay days
    activities = []
    for weather_day in weather_days:
        day_activity = weather_activity.decideWeatherActivity(weather_day)
        activities.append(day_activity)
    
    #Show the user the selected activities for their arrival and subsequent days
    print("\nCongratulations the following activities have been specially chosen for you:")
    for activity in activities:
        print(f"    {activity}")
        
    # If the user choses a valid date but the number of stay days will go beyond the dates in the dataset
    # print a message to the user informing them of this
    if int(stay_days) > len(activities):
        print("WARNING:  Your stay goes beyond the last valid holiday date")
        print("Hitchhiker's Guide recommends blasting off from the planet before this")
    

print("~"*40)
print("  HITCHHIKER'S GUIDE TO THE RED PLANET")
print("~"*40)
main()


