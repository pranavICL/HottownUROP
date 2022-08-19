##Pranav and Cesca, HOTTOWN simulation

import csv
from datetime import date
from datetime import datetime
import datetime

global maxindex = 24

##input the date that you would like to 
date = input("what date would you like to simulate? from 2019")
startval = str(date + '00:00')


##reading the csv and comparing it with current datetime in 2019
file = open('ninjadata3.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader) 
header
rows = []
dt = []
energy = []
outsidetemperature = []
for row in csvreader:
    rows.append(row)
    dt.append(row[0])
    energy.append(row[1])
    outsidetemperature.append(row[1])
    
rows
file.close()

##finding the index values in order to find the solar input
##this is the start of the day in question
index = dt.index(startval) 
print(index)
simenergy = energy[index]
print(simenergy)

#creating a list of all the datys values

def daysdata(index):
    solar = []
    for i in range(maxindex):
        solar[i] = energy[index+i]


##the general working of the electricity sim and battery in watt hours
battery = 4000*60*60
batterymax = 10;
demand = 10

##calculating demand

def probability(percentage):
    number = randint(100)
    if number<percentage:
        return True
    else return False

def repeated(global minutesperinterval, index):
    index2 = (24*60)/minutesperintervals
    index3 = 24/index2
    if index%index2 == 0:
        return True
    else return False

def timetoindex(hour, minute, maxindex):
    

def active(time, degradationconst, status):
    

def probabilitydegradation

            

##the general functionality of the simulation
demand = 5
simenergy = 10
battery = 5
grid = demand - simenergy
if simenergy>demand:
    battery = battery + (simenergy - demand)
if simenergy<demand:
    if battery>0:
        requirement = demand - simenergy
        if requirement>battery:
            demand = demand - battery
            battery = 0
        else:
            battery = battery - demand
            demand = 0

