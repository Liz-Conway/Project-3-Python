'''
Created on 6 Dec 2021

@author: Liz-Conway
'''

from DateUtil import DateUtil
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
        
    def load(self):
        self.loaded_data = open(self.csv_file, 'r')
        #Remove header line
        next(self.loaded_data)
        
        for line in self.loaded_data :
            # print("~~~~")
            # print(line)
            sol_weather = line.split(',')
            i = 0
            # for datum in sol_weather:
            #     print(str(i) + ":  " + datum)
            #     i+=1
            dateUtil = DateUtil()
            solDate = dateUtil.stringToDate(sol_weather[1])
            solTemp = int(sol_weather[6])
            solPressure = int(sol_weather[7])
            solOpacity = sol_weather[9].rstrip()    # remove newline character
            
            daySol = Sol(solDate, solTemp, solPressure, solOpacity)
            
            self.weather.append(daySol)
        
        print(self.weather)