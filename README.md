# Raspberry-Pi-CPU-Temps
A python script for monitoring raspberry pi cpu temps from within a terminal

The script runs in python3 and requires the GPIOZero & Time libraries for the raspberry pi

By default the script will keep writing temperatures until you stop the program.
There are commented out sections of code to enable you to only print a specific number of lines if you wish.


## How To Use:
Download the cpu_temps.py file
Navigate to the downloaded file within a terminal
Enter the following into the terminal:
```
python3 cpu_temps.py
```

## How To Stop:
When the program is running in the terminal, press "Ctrl + C" to stop the code.


## How To Change Mode:
By default the code runs infinitely. To change this simply Comment out the infinite loop and uncomment the Limited number of lines loop.
It was written in two different functions for beginners to read easier and alter while preserving the other parts of code for easy switching between modes.

Simply Change:
```
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
```
to 
```
from gpiozero import CPUTemperature
from time import sleep

#counter
printCount = 0

#Infinite loop
#while True:
#	# gets cpu temperature
#	temp = CPUTemperature()
#
#	#rounds temperature to 1 decimal place 
#	cpu_temp = round(temp.temperature,1)
#
#	#prints the temperature
#	print(str(cpu_temp)+"°C") 
#	
#	# number of seconds before re-running the function
#	sleep(2) 

#Limited number of lines
while (printCount <= 20): #20 is the maximum number of lines you want to print
	# gets cpu temperature
	temp = CPUTemperature()

	#rounds temperature to 1 decimal place 
	cpu_temp = round(temp.temperature,1)

	#prints the temperature
	print(str(cpu_temp)+"°C") 
	
	#increments the print count
 	printCount = (printCount + 1)

	# number of seconds before looping the function
	sleep(2)
```

I supppose you could be lazy and copy/paste the above into the python file or create a second file to have one of each function.

Enjoy!
