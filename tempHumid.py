'''
temprature,Humid get class
'''

import time
import dht11
import RPi.GPIO as GPIO


#define GPIO 18 as DHT11 data pin
Temp_sensor = 18

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	instance = dht11.DHT11(Temp_sensor)

	while True:
		result = instance.read()
		if result.temperature != 0 and result.humidity != 0 :
			print" temperature = ",result.temperature,"C","Humidity = ",result.humidity,"%"

		time.sleep(1)

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
