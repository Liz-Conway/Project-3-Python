'''
Created on 7 Dec 2021

@author: Liz-Conway
'''
from LoadData import LoadData

def main():
    '''
    Launch point for the Hitchhiker's Guide to the Red Planet
    '''
    print("Loading weather_data!!!")
    load_data = LoadData('../mars-weather.csv')
    load_data.load()
    print("Data loaded successfully!")
    weather_data = load_data.weather
    print(weather_data[0])
    

print("~"*40)
print(" Hitchhiker's Guide to the Red Planet")
print("~"*40)
main()


