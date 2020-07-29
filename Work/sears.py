#sears.py 

#Initialize
#num_bills = 1
#day = 1
#b_height = 0.11*0.001 #Meters
#sears = 442 #Meters
#
##Run
#while num_bills * b_height < sears:
	#print(day, num_bills, num_bills*b_height)
	#day = day + 1
	#num_bills = num_bills*2
#
#print('Number of days: ', day)
#print('Number of bills: ', num_bills)
#print('Final height: ', num_bills*b_height)


# INCORRECT CODE 

bill_thickness = 0.11 * 0.001    # Meters (0.11 mm)
sears_height   = 442             # Height (meters)
num_bills      = 1
day            = 1

while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
print('Number of bills', num_bills)
print('Final height', num_bills * bill_thickness)