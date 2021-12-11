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
        self.max_pressure = -999    # Temporary max pressure - deliberately very low
        self.min_pressure = 9999    # Temporary min pressure - deliberately very high
        
    def load(self):
        self.loaded_data = open(self.csv_file, 'r')
        #Remove header line
        next(self.loaded_data)
        
        for line in self.loaded_data :
            sol_weather = line.split(',')
            dateUtil = DateUtil()
            solDate = dateUtil.stringToDate(sol_weather[1])
            try:
                solTemp = int(sol_weather[6])
                if solTemp > self.max_temp :
                    self.max_temp = solTemp
                if solTemp < self.min_temp :
                    self.min_temp = solTemp
            except ValueError as ve :
                solTemp = "NaN"
                
            try:    
                solPressure = int(sol_weather[7])
                if solPressure > self.max_pressure :
                    self.max_pressure = solPressure
                if solPressure < self.min_pressure :
                    self.min_pressure = solPressure
            except ValueError as ve :
                    solPressure = "NaN"
            solOpacity = sol_weather[9].rstrip()    # remove newline character
            
            daySol = Sol(solDate, solTemp, solPressure, solOpacity)
            
            self.weather.append(daySol)
        
    def get_median_temperature(self):
        return (self.max_temp + self.min_temp) // 2
    
    def get_median_air_pressure(self):
        return(self.max_pressure + self.min_pressure) // 2
        
    def search_for_day(self, search_date):
        sol_day = DateUtil().stringToDate(search_date)
        
        for sol in self.weather:
            if sol.earth_date == sol_day :
                return sol
            
        return "Sol not found in weather data"