##a program to read the database and take the average of the hours at each individual hour datapoint

import csv
from datetime import date
from datetime import datetime

##this reads the current date and time and matches it with the corresponding data from that datetime in 2019
time = 1100;
today = date.today()
now = datetime.now()

file = open('ninjadata3.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
dt = []
energy = []
for row in csvreader:
    rows.append(row)
    dt.append(row[0])
    energy.append(row[1])
rows
file.close()

d1 = today.strftime("%d/%m")
simdate = str(d1+ '/2019')
simtime = str(now.strftime("%H:")+"00")
dattime = str(simdate + ' ' + simtime)
print(dattime)

index = dt.index(dattime)
print(index)
simenergy = energy[index]
print(simenergy)

##the general working of the electricity sim and battery 
battery = 0
batterymax = x;
demand = 10

## calculating demand
toothbrush
washing machine
kettle
dryer
dishwasher
microwave
TV

file = open('data.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
dt = []
demand = []
for row in csvreader:
    rows.append(row)
    dt.append(row[0])
    demand.append(row[1])
rows
file.close()

def likelihood(prob):
    
##

battery = 4/5 kWh
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
