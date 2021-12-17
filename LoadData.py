'''
Created on 6 Dec 2021

@author: Liz-Conway
'''

from DateUtil import DateUtil
from datetime import date

from Sol import Sol


class LoadData():
    '''
    classdocs
    '''

    def __init__(self, csv_file):
        '''
        Constructor
        '''
        self.csv_file = csv_file
        self.weather = []
        self.max_temp = -999    # Temporary max temp - deliberately very low
        self.min_temp = 999    # Temporary min temp - deliberately very high
        self.max_pressure = -999    # Temp. max pressure - deliberately v. low
        self.min_pressure = 9999    # Temp. min pressure - deliberately v. high

    def load(self):
        self.loaded_data = open(self.csv_file, 'r')
        # Remove header line
        next(self.loaded_data)

        for line in self.loaded_data:
            sol_weather = line.split(',')
            dateUtil = DateUtil()
            solDate = dateUtil.string_to_date(sol_weather[1])
            try:
                solTemp = int(sol_weather[6])
                if solTemp > self.max_temp:
                    self.max_temp = solTemp
                if solTemp < self.min_temp:
                    self.min_temp = solTemp
            except ValueError as e:
                solTemp = "NaN"

            try:
                solPressure = int(sol_weather[7])
                if solPressure > self.max_pressure:
                    self.max_pressure = solPressure
                if solPressure < self.min_pressure:
                    self.min_pressure = solPressure
            except ValueError as e:
                    solPressure = "NaN"
            solOpacity = sol_weather[9].rstrip()    # remove newline character

            daySol = Sol(solDate, solTemp, solPressure, solOpacity)

            self.weather.append(daySol)

    def get_median_temperature(self):
        return (self.max_temp + self.min_temp) // 2

    def get_median_air_pressure(self):
        return(self.max_pressure + self.min_pressure) // 2

    def search_for_day(self, search_date):
        sol_day = DateUtil().string_to_date(search_date)

        for sol in self.weather:
            if sol.earth_date == sol_day:
                return sol

        raise IndexError(f"No weather data found for {search_date}")

    def search_for_days(self, search_date, days):
        sol_first_day = DateUtil().string_to_date(search_date)
        # sol_index in the weather list where we find the first day
        sol_index = 0

        sols = []
        # Use this for loop to get the sol_index in
        # self.weather list of the search date
        for sol in self.weather:
            if sol.earth_date == sol_first_day:
                # Found it at sol_index
                # So breaking out of the for loop here
                # means variable sol_index is the index of the day
                # that we are looking for
                break

            # if the days do not match
            # increment sol_index and the for loop will get the next Sol
            sol_index += 1

        # Since the data goes from latest day first to the earliest day last,
        # i.e. in reverse order
        # we take the number of days away from the found index
        # to get the last day to return
        latest_index = sol_index - int(days) + 1
        # If the latest index is negative
        # this means we have gone past the start of the data
        # so set the latest index to be zero
        # (The very last entry in the data set)
        if latest_index < 0:
            latest_index = 0

        earliest_index = sol_index + 1

        # Use this for loop to retrieve the Sol for each day
        # Data is in reverse date order,
        # i.e. latest date first, earliest date last
        # Use 'reversed' for the range to go from the
        # higher (earliest) index to the lower (latest)
        for i in reversed(range(latest_index, earliest_index)):
            sol = self.weather[i]
            sols.append(sol)

        return sols
