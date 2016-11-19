#!/usr/bin/python2.7

import sys, os, math


def soundFree():
	userChoice = raw_input("\n\nDo you want to know the frequency, speed or wavelength?\n\n    1. Frequency\n    2. Wavelength\n    3. Speed\n\n")


	if userChoice == "1":
		wavelength = raw_input("\nWavelength [m] = ")
		speed = raw_input("\nSpeed [m/s] = ")
		try:
			wavelength = float(wavelength)
			speed = float(speed)
			frequency = round(speed/wavelength, 3)
			print "\nFrequency [Hz] = "+str(frequency)
		except:
			print "Please, next time type in a number"
			sys.exit()

	elif userChoice == "2":
		frequency = raw_input("\nFrequency [Hz] = ")
		speed = raw_input("\nSpeed [m/s] = ")
		try:
			frequency = float(frequency)
			speed = float(speed)
			wavelength = round(speed/frequency, 3)
			print "\nWavelength [m] = "+str(wavelength)
		except:
			print "Please, next time type in a number"
			sys.exit()

	elif userChoice == "3":
		wavelength = raw_input("\nWavelength [m] = ")
		frequency = raw_input("\nFrequency [Hz] = ")
		try:
			wavelength = float(wavelength)
			frequency = float(frequency)
			speed = round(wavelength*frequency, 3)
			print "\nSpeed [m/s] = " +str(speed)
		except:
			print "Please, next time type in a number"
			sys.exit()


	else:
		print "Please, don't try to break the system :)"


	hearSound = raw_input("Would you want to hear how amazing does this frequency sounds like? [Y/N]")
	if hearSound == "y":
		shell = "aoss swgen -x10 1 "+str(int(frequency))+"0 "+str(int(frequency))+"0"
		os.popen(shell)
		print "\nThank you for using soundwave, enjoy the annoying sound you chose >:D\n\nTip: To recover your ears, please press Ctrl+Z ;)"
	elif hearSound == "n":
		print "\nThank you for using soundwave :D"		



def soundWSpeed():
	userChoice = raw_input("\n\nDo you want to know the frequency or wavelength?\n\n    1. Frequency\n    2. Wavelength\n\n")
	speed = 343

	if userChoice == "1":
		wavelength = raw_input("\nWavelength [m] = ")
		
		try:
			wavelength = float(wavelength)
			speed = float(speed)
			frequency = round(speed/wavelength, 3)
			print "\nFrequency [Hz] = "+str(frequency)
		except:
			print "Please, next time type in a number when entering the wavelength value"
			sys.exit()

	elif userChoice == "2":
		frequency = raw_input("\nFrequency [Hz] = ")
		try:
			frequency = float(frequency)
			speed = float(speed)
			wavelength = round(speed/frequency, 3)
			print "\nWavelength [m] = "+str(wavelength)
		except:
			print "Please, next time type in a number when entering the frequency value"
			sys.exit()

	else:
		print "Please, don't try to break the system :)"


	hearSound = raw_input("Would you want to hear how amazing does this frequency sounds like? [Y/N]")
	if hearSound == "y":
		shell = "aoss swgen -x10 1 "+str(int(frequency))+"0 "+str(int(frequency))+"0"
		os.popen(shell)
		print "\nThank you for using soundwave, enjoy the annoying sound you chose >:D\n\nTip: To recover your ears, please press Ctrl+Z ;)"
	elif hearSound == "n":
		print "\nThank you for using soundwave :D"



def light():
	userChoice = raw_input("\n\nDo you want to know the frequency or wavelength?\n\n    1. Frequency\n    2. Wavelength\n\n")
	speed = 3*10**8

	if userChoice == "1":
		wavelength = raw_input("\nWavelength [m] = ")
		try:
			wavelength = float(wavelength)
			speed = float(speed)
			frequency = round(speed/wavelength, 3)
			print "\nFrequency [Hz] = "+str(frequency)
		except:
			print "Please, next time type in a number"
			sys.exit()

	elif userChoice == "2":
		frequency = raw_input("\nFrequency [Hz] = ")
		try:
			frequency = float(frequency)
			speed = float(speed)
			wavelength = round(speed/frequency, 3)
			print "\nWavelength [m] = "+str(wavelength)
		except:
			print "Please, next time type in a number"
			sys.exit()

	else:
		print "Please, don't try to break the system :)"
	
	if wavelength < 4.5*10**-7:
		print "Light colour = Violet\n\n"
	elif wavelength >= 4.5*10**-7 and wavelength < 4.95*10**-7:
		print "Light colour = Blue\n\n"
	elif wavelength >= 4.95*10**-7 and wavelength < 5.7*10**-7:
		print "Light colour = Green\n\n"
	elif wavelength >= 5.7*10**-7 and wavelength < 5.9*10**7:
		print "Light colour = Yellow\n\n"
	elif wavelength >= 5.9*10**-7 and wavelength < 6.2*10**-7:
		print "Light colour = Orange\n\n"
	elif wavelength >= 6.2*10**-7:
		print "Light colour = Red\n\n"
	


def electromagnetic():
	userChoice = raw_input("\n\nDo you want to know the frequency or wavelength?\n\n    1. Frequency\n    2. Wavelength\n\n")
	speed = 3*10**8

	if userChoice == "1":
		wavelength = raw_input("\nWavelength [m] = ")
		try:
			wavelength = float(wavelength)
			speed = float(speed)
			frequency = round(speed/wavelength, 3)
			print "\nFrequency [Hz] = "+str(frequency)
		except:
			print "Please, next time type in a number"
			sys.exit()

	elif userChoice == "2":
		frequency = raw_input("\nFrequency [Hz] = ")
		try:
			frequency = float(frequency)
			speed = float(speed)
			wavelength = round(speed/frequency, 3)
			print "\nWavelength [m] = "+str(wavelength)
		except:
			print "Please, next time type in a number"
			sys.exit()

	else:
		print "Please, don't try to break the system :)"
	
	if wavelength < 10**-1:
		print "Light colour = Radio wave\n\n"
	elif wavelength >= 10**-1 and wavelength < 10**-3:
		print "Light colour = Microwave\n\n"
	elif wavelength >= 10**-3 and wavelength < 10**-6.25:
		print "Light colour = Infrared\n\n"
	elif wavelength >= 10**-6.25 and wavelength < 10**6.75:
		print "Light colour = Visible light\n\n"
	elif wavelength >= 10**6.75 and wavelength < 10**-8:
		print "Light colour = Ultraviolet\n\n"
	elif wavelength >= 10**-8 and wavelength < 10**-11:
		print "Light colour = X-Rays\n\n"
	elif wavelength >= 10**-11:
		print "Light colour = Gamma rays\n\n" 

def interference():
	interference = raw_input("\n\nFor interferences, just a couple of things are needed:\n\n	1) Distance between sources\n	2) Wavelength/Frequency\n	3) Speed\n\n[Press Enter to continue]\n\n")	
	distance = raw_input("Distance between sources [cm] = ")
	speed = raw_input("Speed [m/s] = ")
	userChoice = raw_input("Now, if you know the frequency, type [1].\nIf in the other hand you know the wavelength, type [2].")
		
	if userChoice == "1":
		frequency = raw_input("\nFrequency [Hz] = ")
		frequency = float(frequency)
		speed = float(speed)
		distance = float(distance)
		wavelength = float(speed/frequency)
		calc = (distance*frequency)/speed
		calc1 = round(calc/100)
		k = calc1*2 + 1

		print "\nNumber of constructive interferences = "+str(k)
		
		user = raw_input("Would you want to continue and calculate the angles at which these interferences are formed? [y/n]")
		if user == "y":
			calcK = raw_input("Please type in the number of the interference:	")
			k = int(calcK)
			b = float(distance/100)
			wl = float(wavelength)
			radians = math.asin((k*wl) / b)
			angle1 = math.degrees(radians)
			print "\n\n\n\nThe angle for interference #"+str(k)+" =		"+str(angle1)
		elif user == "n":
			print "\n\nThank you for using the ultimate wave calculator :)"
		

	elif userChoice == "2":
		wavelength = raw_input("\nWavelength [m] = ")
		try:
			wavelength = float(wavelength)
			speed = float(speed)
			distance = float(distance)
			frequency = float(speed/wavelength)
			k = round((distance*frequency)/speed)

			print "\nNumber of constructive interferences = "+str(k)
			
			user = raw_input("Would you want to continue and calculate the angles at which these interferences are formed? [y/n]")
			if user == "y":
				userAngle = raw_input("Please type in the number of the interference:	")
				k = int(userAngle)
				b = float(distance)
				wl = float(wavelength)
				angle = math.asin(k*wl/b)
				angle1 = math.degree(angle)
				print "\n\n\n\nThe angle for interference #"+str(k)+" =		"+str(angle1)
			elif user == "n":
				print "\n\nThank you for using the ultimate wave calculator :)"
				
		except:
			sys.exit()

		
			

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


user = raw_input("\n~Welcome to the ultimate wave calculator.\n~What would you like to play with?\n\n	1) Electromagnetic\n	2) Light\n	3) Sound(With predefined speed)\n	4) Sound(Free)\n	5) Interferences\n\n")

if user == "1":
	electromagnetic()

elif user == "2":
	light()

elif user == "3":
	soundWSpeed()

elif user == "4":
	soundFree()

elif user == "5":
	interference()


