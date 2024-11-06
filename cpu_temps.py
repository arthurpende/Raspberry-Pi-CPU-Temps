from gpiozero import CPUTemperature
from time import sleep

#counter
printCount = 0

#Infinite loop
while True:
	# gets cpu temperature
	temp = CPUTemperature()

	#rounds temperature to 1 decimal place 
	cpu_temp = round(temp.temperature,1)

	#prints the temperature
	print(str(cpu_temp)+"°C") 
	
	# number of seconds before re-running the function
	sleep(2) 

#Limited number of lines
#while (printCount <= 20): #20 is the maximum number of lines you want to print
#	# gets cpu temperature
#	temp = CPUTemperature()
#
#	#rounds temperature to 1 decimal place 
#	cpu_temp = round(temp.temperature,1)
#
#	#prints the temperature
#	print(str(cpu_temp)+"°C") 
#	
#	#increments the print count
# 	printCount = (printCount + 1)
#
#	# number of seconds before looping the function
#	sleep(2)