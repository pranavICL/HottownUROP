c = 1.005 (kJ/(kg⋅C))
Req = 4 #found on google [(m2.K)/W]
width = 4
length = 5
height = 2.5
rho = 1.225/1000
Mair = width*length*height*rho #units
wall_area = 
heat_watts = 2*2112

#test
#water heaters to get gas money
#efficiency
#moneys 

#joules used by radiators for day
def thermal(heater,temp,outside_temp):
    seconds_in_a_day = 86400
    interval_duration = 600
    intervals = seconds_in_a_day/interval_duration
    thermal_energy_usage = 0
    # decide heater on/off
    if (temp < 18) or (heater = 1):
        heater = 1
    if (temp > 22) or (heater = 0):
        heater = 0
    # calculate energy in/out        
    heat_lost = (temp - outside_temp) / Req  * interval_duration * wall_area # joules 
    if (heater = 1) :
        heat_gain = heat_watts * interval_duration #joules 
    else:
        heat_gain/t = 0
    # calculate new temp
    change_in_temp = ( ( 1/(Mair*c) ) * (heat_gain - heat_lost) ) #cels
    temp = temp + change_in_temp #cels
    return temp , heater
            
        

