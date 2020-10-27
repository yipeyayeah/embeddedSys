#!/usr/bin/python
import smbus
import time
import Adafruit_DHT
import time
import datetime
import csv
# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value
ONE_TIME_HIGH_RES_MODE = 0x20

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def date_now():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    today = str(today)
    return today

def time_now():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    now = str(now)
    return now

def convertToNumber(data):
    return ((data[1] + (256 * data[0])) / 1.2)

def readLight(addr=DEVICE):
    data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE)
    return convertToNumber(data)

def main():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        print ("Light Level : " + str(readLight()) + " lux")
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
            with open("dataset.csv", mode="a") as sensor_readings:
                sensor_write = csv.writer(
                    sensor_readings, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
                )
                write_to_log = sensor_write.writerow(
                    [date_now(), time_now(), " Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity), " Light Level : " + str(readLight()) + " lux" ]
                )
        else:
            print("Failed to retrieve data from humidity sensor")
        
        time.sleep(300)
if __name__=="__main__":
   main()
