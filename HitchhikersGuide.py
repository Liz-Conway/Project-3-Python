'''
Created on 7 Dec 2021

@author: Liz-Conway
'''
from LoadData import LoadData
from DateValidator import DateValidator
from WeatherActivity import WeatherActivity
from pickle import TRUE

def main():
    '''
    Launch point for the Hitchhiker's Guide to the Red Planet
    '''
    print("....Loading weather_data!!!")
    load_data = LoadData('mars-weather.csv')
    load_data.load()
    print("....Data loaded successfully!\n")
    
    # Loop to get valid date from the user
    while True:
        print("Please enter a date in the format yyyy-mm-dd  E.G. 2015-03-24")
        print("Valid dates are between 2012-08-15 and 2018-02-27")
        search_date = input("What date are you arriving on Mars?\n")
        
        date_validator = DateValidator()
        valid_date = date_validator.validateDate(search_date)
        
        if valid_date :
            # If the date is valid
            # Break out of the while loop and 
            # continue with the rest of the program
            break
        else :
            print(f"\n'{search_date}' is not a valid date")
            # Start the while loop again
            # asking for the date
    
    # If we get here the date is valid, so we can validate the stay_days
    while True:    
        stay_days = input("How many days will you be staying (positive integers only)?\n")
        
        # https://www.pythonpool.com/python-check-if-string-is-integer/
        # isdigit() Only allows positive integers
        valid_days = stay_days.isdigit()
        
        if valid_days :   # Days are valid
            # If the days entered are valid then
            # break out of this while loop and continue running the rest of the program
            # If the days entered is not a positive integer then
            # the while loop will keep looping until a valid stay day is entered
            break
        else :
            print(f"\n'{str(stay_days)}' is not a valid number")
            # Start this while loop again
            # asking for the stay days
            
    while True:
        show_weather = input("Would you like to see the weather details (Y/N)?\n").upper()
        
        if show_weather == "Y" or show_weather == "N" :
            #valid data => continue with the code by breaking out of this while loop
            break
        else:
            print("\nPlease enter only 'Y' or 'N'")
        
    
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
        if show_weather == "Y":
            day_activity += "  " + str(weather_day.temperature) + " degrees"
            day_activity += "  " + str(weather_day.air_pressure) + " Pascal"
            day_activity += "  " + weather_day.opacity
        activities.append(day_activity)
    
    # If the user wants the weather data then display the median temperature and air pressure
    if show_weather == "Y":
        print(f"Median Temperature :  {median_temperature} degrees")
        print(f"Median Air Pressure :  {median_air_pressure} Pascal")
    
    #Show the user the selected activities for their arrival and subsequent days
    print("\nCongratulations the following activities have been specially chosen for you:")
    for activity in activities:
        print(f"    {activity}")
        
    # If the user choses a valid date but the number of stay days will go beyond the dates in the dataset
    # print a message to the user informing them of this
    if int(stay_days) > len(activities):
        print("WARNING:  Your stay goes beyond the last valid holiday date")
        print("Hitchhiker's Guide recommends blasting off from the planet before this")
    
    print("\n Thank you for choosing the Hitchhiker's Guide to the Red Planet")
    print("~"*80)

print("~"*80)
spacer = " "*21
print("~" + spacer + "HITCHHIKER'S GUIDE TO THE RED PLANET" + spacer + "~")
print("~"*80)
print(" Welcome, time-travelling, inter-galactic holiday maker")
print(" For your holiday to Mars (the Red Planet)")
print(" Please choose a valid arrival date and the number of days you will be staying")
print(" Valid arrival dates are between 15th August 2012 and 27th February 2018")
print(" Dates entered must be of the format yyyy-mm-dd")
print(" Enter your stay duration as a positive integer")
print("~"*80)
main()


