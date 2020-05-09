from datetime import datetime
import Adafruit_DHT
import board
import busio
import adafruit_bmp280
import bh1750


humidity_sensor = Adafruit_DHT.DHT11
humidity_sensor_pin = 12
i2c = busio.I2C(board.SCL, board.SDA)
pressure_sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,0x76)
pressure_sensor.sea_level_pressure = 1008.0

def update_sensors(sea_level_pressure = 1008.0):
    pressure_sensor.sea_level_pressure = sea_level_pressure
    timestamp = int(datetime.timestamp(datetime.now()))
    humidity, temperature = Adafruit_DHT.read_retry(humidity_sensor, humidity_sensor_pin)
    altitude = pressure_sensor.altitude
    temperature_bmp = pressure_sensor.temperature
    pressure = pressure_sensor.pressure
    luxlevel = bh1750.readLight()

    return {'timestamp':timestamp, 'humidity': humidity, 'temperature':temperature, 'altitude':altitude,
            'temperature_bmp':temperature_bmp, 'pressure':pressure, 'luxlevel':luxlevel,
            'sea_level_pressure':pressure_sensor.sea_level_pressure}
