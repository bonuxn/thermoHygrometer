'''
LCD data view

'''
import time
import dht11
import i2clcd_driver as LCD
import RPi.GPIO as GPIO
import smbus
import time

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	Temp_sensor = 18
	instance = dht11.DHT11(Temp_sensor)
	i_lcd = LCD.LCD()

	# Initialise display
	# Send some test

	while True:
		result = instance.read()
		if result.temperature != 0 and result.humidity != 0 :
			# print " temperature = ",result.temperature,"C","Humidity = ",result.humidity,"%"

			st_temp = str(result.temperature) + " " + "C"
			st_humid = str(result.humidity) + " " + "%"

			i_lcd.lcd_string(st_temp,i_lcd.LCD_LINE_1)
			i_lcd.lcd_string(st_humid,i_lcd.LCD_LINE_2)

			time.sleep(3)

if __name__=='__main__':
	try:
		main()
	except KeyboardInterrupt:
		pass
