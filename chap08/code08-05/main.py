import time

import dht11
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin=14)
while True:
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        print(f'温度:{temperature}')
        print(f'湿度:{humidity}')
    time.sleep(1)