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

    

        

