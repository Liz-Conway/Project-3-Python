'''
Created on 7 Dec 2021

@author: Liz-Conway
'''
from LoadData import LoadData
from DateValidator import DateValidator
from WeatherActivity import WeatherActivity
from colorama import init, Fore, Back
from colorama.ansi import Style


def main():
    '''
    Launch point for the Hitchhiker's Guide to the Red Planet
    '''
    print(Fore.YELLOW + "....Loading weather_data!!!")
    load_data = LoadData('mars-weather.csv')
    load_data.load()
    print("....Data loaded successfully!\n" + Style.RESET_ALL)

    # Loop to get valid date from the user
    while True:
        date_format = Fore.MAGENTA
        date_format += "Please enter a date in the format "
        date_format += Style.BRIGHT + "yyyy-mm-dd" + Style.RESET_ALL
        date_format += Fore.MAGENTA + "  E.G. 2015-03-24"
        print(date_format)
        valid_dates = "Valid dates are between "
        valid_dates += Style.BRIGHT + "2012-08-15" + Style.RESET_ALL
        valid_dates += Fore.MAGENTA
        valid_dates += " and " + Style.BRIGHT + "2018-02-27"
        valid_dates += Style.RESET_ALL
        print(valid_dates)
        search_input = Fore.BLUE
        search_input += "What date are you arriving on Mars?"
        search_input += Fore.RESET
        search_date = input(search_input + "\n")

        date_validator = DateValidator()
        valid_date = date_validator.validateDate(search_date)

        if valid_date:
            # If the date is valid
            # Break out of the while loop and
            # continue with the rest of the program
            break
        else:
            error_date = "\n" + Back.RED + f"{search_date}" + Back.RESET
            error_date += " is not a valid date"
            print(error_date)
            # Start the while loop again
            # asking for the date

    # If we get here the date is valid, so we can validate the stay_days
    while True:
        # PEP8 Validation split the text string
        # because it goes beyond 80 characters
        days_input = Fore.BLUE + "How many days will you be staying "
        days_input += "(positive integers only)?" + Fore.RESET
        days_input += "\n"
        stay_days = input(days_input)

        # https://www.pythonpool.com/python-check-if-string-is-integer/
        # isdigit() Only allows positive integers
        valid_days = stay_days.isdigit()

        if valid_days:   # Days are valid
            # If the days entered are valid then
            # break out of this while loop and continue running
            # the rest of the program
            # If the days entered is not a positive integer then
            # the while loop will keep looping
            # until a valid stay day is entered
            break
        else:
            error_days = "\n" + Back.RED + f"{str(stay_days)}"
            error_days += Back.RESET + " is not a valid number"
            print(error_days)
            # Start this while loop again
            # asking for the stay days

    while True:
        weather_ip = Fore.BLUE
        weather_ip += "Would you like to see the weather details (Y/N)?"
        weather_ip += Fore.RESET + "\n"
        show_weather = input(weather_ip).upper()

        if show_weather == "Y" or show_weather == "N":
            # valid data => continue with the code by
            # breaking out of this while loop
            break
        else:
            only_y_n = "\nPlease enter only " + Fore.GREEN
            only_y_n += "Y" + Fore.RESET + " or " + Fore.GREEN
            only_y_n += "N" + Fore.RESET
            print(only_y_n)

    # Congratulations you have valid data!!
    # The rest of the program starts here :
    # Retrieve the weather for the entered dates
    try:
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
                temp_col = Fore.CYAN + Style.BRIGHT + Back.BLUE
                press_col = Fore.GREEN + Style.BRIGHT + Back.BLUE
                opacity_col = Fore.LIGHTYELLOW_EX + Back.BLUE
                day_activity += "  " + temp_col 
                day_activity += str(weather_day.temperature) 
                day_activity += " degrees" + Back.RESET
                day_activity += "  " + press_col 
                day_activity += str(weather_day.air_pressure) 
                day_activity += " Pascal" + Back.RESET
                day_activity += "  " + opacity_col 
                day_activity += weather_day.opacity + Fore.RESET + Back.RESET
                day_activity += Style.RESET_ALL
            activities.append(day_activity)
    
        # If the user wants the weather data
        # then display the median temperature and air pressure
        if show_weather == "Y":
            median_temperature_display = "Median Temperature :  "
            median_temperature_display += Fore.CYAN + f"{median_temperature}"
            median_temperature_display += " degrees" + Fore.RESET
            print(median_temperature_display)
            median_pressure_display = "Median Air Pressure :  "
            median_pressure_display += Fore.GREEN + f"{median_air_pressure}"
            median_pressure_display += " Pascal" + Fore.RESET
            print(median_pressure_display)
            
        # PEP8 Validation split the text string
        # because it goes beyond 80 characters
        congrats = "\nCongratulations the following activities"
        congrats += " have been specially chosen for you:"
        # Show the user the selected activities for their
        # arrival and subsequent days
        print(congrats)
        for activity in activities:
            print(f"    {activity}")
    
        # If the user choses a valid date but the number of stay days
        # will go beyond the dates in the dataset
        # print a message to the user informing them of this
        if int(stay_days) > len(activities):
            beyond_last_valid = Back.RED
            beyond_last_valid += "WARNING:  Your stay goes beyond "
            beyond_last_valid += "the last valid holiday date"
            print(beyond_last_valid)
            # PEP8 Validation split the text string
            # because it goes beyond 80 characters
            blast_off = "Hitchhiker's Guide recommends blasting off "
            blast_off += "from the planet before this" + Back.RESET
            print(blast_off)

    except IndexError as e:
        warning = "\n" + Back.RED + Fore.BLACK
        warning += f"Mars Rover was not operational on {search_date}\n"
        warning += "There is no data available for this arrival date"
        warning += Style.RESET_ALL
        print(warning)

    print("\n Thank you for choosing the Hitchhiker's Guide to the Red Planet")
    print(title + "~"*80 + Style.RESET_ALL)

init()
# from colorama import Fore, Back, Style
title = Back.RED + Fore.LIGHTMAGENTA_EX + Style.BRIGHT
print(title)
# print(Back.GREEN + "& with a green background")
# print(Style.DIM + "Dimmed text")
# print(Style.RESET_ALL)
print("~"*80)
spacer = " "*21
print("~" + spacer + "HITCHHIKER'S GUIDE TO THE RED PLANET" + spacer + "~")
print("~"*80)
print(" Welcome, inter-galactic, time-travelling tourist")
print(" For your holiday to Mars (the Red Planet)")
print(Style.RESET_ALL)
instruction = Fore.RED
# PEP8 Validation split the text string
# because it goes beyond 80 characters
# blue_on_yellow = Fore.BLUE + Back.YELLOW
instructions = instruction + " Please choose a valid arrival date "
#instructions += blue_on_yellow + "Blue on Yellow" + Style.RESET_ALL
instructions += "and the number of days you will be staying"
print(instructions)
valid_dates = " Valid arrival dates are between "
valid_dates += Back.LIGHTMAGENTA_EX + "15th August 2012" + Back.RESET
valid_dates += " and " + Back.LIGHTMAGENTA_EX + "27th February 2018" + Back.RESET
print(valid_dates)
date_format = " Dates entered must be of the format "
date_format += Style.BRIGHT + "yyyy-mm-dd" + Style.NORMAL
print(date_format)
enter_duration = " Enter your stay duration as a "
enter_duration += Style.BRIGHT + "positive integer" + Style.NORMAL
print(enter_duration)
print(Style.RESET_ALL + title + "~"*80 + Style.RESET_ALL)
main()
