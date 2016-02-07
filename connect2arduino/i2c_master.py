# Connect raspberry pi as master and arduino (0x004) as slave via I2C
# Check the corresponding Arduino sketch
# Get numbers from keyboard and send them via I2C bus to arduino
# Arduino uses this numbers to print a message in serial monitor and sends
# confirmation back to RPi. If number is 1, Arduino switches ON or OFF the 
# led in pin 13
 
import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
	bus.write_byte(address, int(value))
	# bus.write_byte_data(address, 0, value)
	return -1

def readNumber():
	number = bus.read_byte(address)
	# number = bus.read_byte_data(address, 1)
	return number

while True:
	var = input("Enter 1 – 9: ")
	if not var:
		continue

	writeNumber(var)
	print("RPI: Hi Arduino, I sent you ", var)
	# sleep one second
	time.sleep(1)

	number = readNumber()
	print("Arduino: Hey RPI, I received a digit ", number)
