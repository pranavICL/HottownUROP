##Pranav and Cesca, HOTTOWN simulation

import csv
from datetime import date
from datetime import datetime
import datetime
import numpy as np
from scipy.stats import norm
from random import randint


maxindex = 24

## GAS VS ELECTRIC VARIABLES

##true means that they are using electricity not gas
boiler = True
shower = True

# gas code

c = 1005 #(J/(kg⋅C))
Req_W = (0.030*2*3.625)+(0.88*2) # 2 layers of bricks plus 1 layer of 2in insulation
Req_C = 0.1875*0.44 + 0.88*2 #asphalt roof plus 2in insulation
Req_F = 0.12*0.5  #1/2in hardwood floor 
width = 4 #m
length = 5 #m
height = 2.5 #m
rho = 1.222 #kg/m3
Mair = width*length*height*rho #kg 
wall_area = height*length*2 + height*width*2 #m2
celing_area = width*length
heat_watts = 1026*2#W
seconds_in_a_day = 86400
interval_duration = 600
intervals = seconds_in_a_day/interval_duration
thermal_energy_usage = 0 #initial
heat_lost =0
heat_gain =0
boiler_heat = 24000 #w
boiler_efficiency = 0.9
boiler_radiator = boiler_efficiency*boiler_heat #watts boiler to radiator
price_gas_KWh = 7.37 #pence
heater = 0

#cost for 88 seconds of radator at 24000  watt hours of gas
#88 seconds = 586.6 watts hours
#costs 4.32p
 

#joules used by radiators for day
def thermal(heater,temp,outside_temp,interval_duration,wall_area):
    # decide heater on/off    
    if (temp < 18) or (heater == 1):
        heater = 1
    if (temp > 22) or (heater == 0):
        heater = 0
    # calculate energy in/out
    
    heat_lost = (( ((temp - outside_temp)*interval_duration*wall_area) / Req_W ) +  (((temp - outside_temp)*interval_duration*celing_area) / Req_C ))+ (((temp - outside_temp)*interval_duration*celing_area) / Req_F ) # walls
    print("heat lost = " ,heat_lost)
    if (heater == 1) :
        heat_gain = heat_watts*interval_duration #joules 
    else:
        heat_gain = 0
    print("heat_gain = " , heat_gain)
    print("Mair = " , Mair)
    # calculate new temp
    change_in_temp = ( (heat_gain - heat_lost)/(Mair*c) ) #cels
    temp = temp + change_in_temp #cels
    print("temp change = " , change_in_temp)
    print("new temp = " , temp)
    return temp , heater
            

#a = thermal(heater,temp[i],outside_temp[i],interval_duration,wall_area)
thermal(0,17,12,interval_duration,wall_area)
Total_day_watts = heat_watts * heater_counter
boiler_time = (Total_day_watts * interval_duration)/boiler_radiator
hours = boiler_time/3600
kwhours = hours*24000
cost = kwhours*price_gas_KWh

##                                  FUNCTIONS


#creating a list of all the days values for energy produced by the solar panels. this works. 
def daysdata(index, maxindex):
    solar = []
    print(index)
    for i in range( 0, int(maxindex)):
        print(i)
        solar.append(energy[int(int(index)+i)])
        solar.append(energy[int(int(index)+i)])
        i = i+1
    return solar
    

##nwo need to filter out the data we dont want and create a smaller list,
## for solar this is likely to be 24
##def timetoindex(hour, minute, maxindex):
##    if minute%60 == 0:
##        index = hour - 1
##        return index
##    else:
##        bigindex = (60/minutes)*24
##        index = hour*(60/minutes)+
####need to complete this function

def probability(percentage):
    number = randint(0, 100)
    if number<int(100*percentage):
        return True
    else: return False
        
    
#Creating a normal distribution Function.
##numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)
##def normal(timenow, timeexpected  sd, maxindex):
##    data = np.arange(1,maxindex,0.01)
##    pdf = norm.pdf(data , loc = timeexpected , scale = 1 )
##      
##    cdf_upper_limit = norm(loc = timeexpected , scale = 1).cdf(timenow+1)
##    cdf_lower_limit = norm(loc = timeexpected , scale = 1).cdf(timenow)
##     
##    prob = cdf_upper_limit - cdf_lower_limit
##    return(prob)

def demanditem(rating, demand):
    demand = demand + rating
    return demand

##                          MAIN BODY

##input the date that you would like to check
date = input("what date would you like to simulate? from 2019")
startval = str(date + ' 00:00')
print(startval)


##reading the csv and writing the data to lists
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
##this is the start of the day in question and will add all the data from that day to simenergy 
index = dt.index(startval) 
print(index)
simenergy = energy[index]
print(simenergy)

solar = daysdata(index, 24)
print(solar)
##calculating demand

TV = []
kettle = []
fridge = []
washingmachine = []
##recency = [TV, kettle, fridge, washingmachine]
recency = [0, 0, 0, 0]
##now we populate all the probabilities for each of the appliences
#for(i in range len(solar)):
#    TV[i] = normal(i, 3, sd, len(solar))
#    kettle[i] = normal(i, 5, sd, len(solar))
#    fridge[i] = normal(i, 5, sd, len(solar))
#    washingmachine[i] = normal(i, 5, sd, len(solar))
 #   i++

#the probability tables of all the appliances, instead of the normal distribution, we can change these to whatever matches the first dataset best
TV = [0.4, 0.4, 0.1,0.1, 0.05, 0.05, 0.01, 0.01, 0.01, 0.01,
      0.01, 0.01, 0.1, 0.3, 0.3, 0.3, 0.4, 0.3,
      0.01,0.01,0.01,0.01, 1,1,1,1,0.01,0.01,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.4, 0.4, 0.3, 0.4]
kettle = [0.01, 0.01, 0.01,0.01, 0.05, 0.05, 0.01, 0.01,
      0.01, 0.01, 0.01, 0.01, 0.1, 0.3, 0.3, 0.8, 0.9, 0.8,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.1, 0.1, 0.1, 0.6, 0.7, 0.8, 0.8, 0.8, 0.8, 0.4]
fridge = [0.4, 0.4, 0.1,0.1, 0.05, 0.05, 0.01, 0.01, 0.01,
      0.01, 0.01, 0.01, 0.1, 0.3, 0.3, 0.3, 0.4, 0.3,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.4, 0.4, 0.3, 0.4]
washingmachine = [0.4, 0.4, 0.1,0.1, 0.05, 0.05, 0.01, 0.01, 0.01,
      0.01, 0.01, 0.01, 0.1, 0.3, 0.3, 0.3, 0.4, 0.3,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,0.01,
      0.6, 0.7, 0.5, 0.6, 0.7, 0.8, 0.4, 0.4, 0.3, 0.4]

##calculating demand
washingmachinerating = 100
kettlerating = 100
TVrating = 200
fridgerating = 50

global demand
demand = 0
##now that the probabilities have been mapped, we can account for the recency factor
for i in range(maxindex*2+1):
    if probability(TV[i]) == True:
        recency[0] = 1
        demanditem(TVrating, demand)
        recency[0] = 1
        print('TV bang')
        for j in range(i, maxindex*2):
            if(TV[j]>0.1 and recency[0] == 1):
                print(TV)
                TV[j] = 0.1
                print('yes ')
                print(TV)
                print(' ')
            elif(TV[j]<=0.1 and recency[0] == 1):
                recency[0] = 0
                print('no')
                print(TV)
            j = j+1
##            print(j)
    if probability(kettle[i]) == True:
        recency[1] = 1
        demanditem(kettlerating, demand)
        k = i
        for k in range(i, maxindex):
            if(kettle[k]>0.1 and recency[1] == 1):
                kettle[i] = 0.1
            elif(kettle[k]<=0.1 and recency[1] == 1):
                recency[1] = 0
            k = k+1
    if probability(fridge[i]) == True:
        recency[2] = 1
        l = i
        demanditem(fridgerating, demand)
        for l in range(i, maxindex):
            if(fridge[l]>0.1 and recency[2] == 1):
                fridge[i] = 0.1
            elif(fridge[l]<=0.1 and recency[2] == 1):
                recency[2] = 0
            l = l+1
    if probability(washingmachine[i]):
        recency[3] = 1
        m = i
        demanditem(washingmachinerating, demand)
        for m in range(i, maxindex):
            if(washingmachine[m]>0.1 and recency[1] == 1):
                washingmachine[i] = 0.1
            elif(washingmachine[m]<=0.1 and recency[1] == 1):
                recency[3] = 0
            m = m+1
    else:
        print('hello ', i, ' ', demand)
    i = i+1


##the general functionality of the simulation

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

