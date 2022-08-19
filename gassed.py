c = 1.005 #(kJ/(kg⋅C))
Req = 4 #found on google [(m2.K)/W]
width = 4 #m
length = 5 #m
height = 2.5 #m
rho = 1.222 #kg/m3
Mair = width*length*height*rho #kg 
wall_area = height*length*2 + height*width*2 #m2
heat_watts = 4224 #W
seconds_in_a_day = 86400
interval_duration = 600
intervals = seconds_in_a_day/interval_duration
thermal_energy_usage = 0 #initial
heat_lost =0
heat_gain =0
#test
#water heaters to get gas money
#efficiency?
#cost of gas (variable)

#joules used by radiators for day
def thermal(heater,temp,outside_temp,interval_duration,wall_area):
    # decide heater on/off    
    if (temp < 18) or (heater == 1):
        heater = 1
    if (temp > 22) or (heater == 0):
        heater = 0
    # calculate energy in/out
    
    heat_lost = ((temp - outside_temp) / Req ) * interval_duration * wall_area # joules
    print("heat lost = " ,heat_lost)
    if (heater == 1) :
        heat_gain = heat_watts * interval_duration #joules 
    else:
        heat_gain = 0
    print("heat_gain = " , heat_gain)
    # calculate new temp
    change_in_temp = ( ( 1/(Mair*c) ) * (heat_gain - heat_lost) ) #cels
    temp = temp + change_in_temp #cels
    print("temp change = " , change_in_temp)
    print("new temp = " , temp)
    return temp , heater
            

a = thermal(0,17,12,interval_duration,wall_area)

    

        

