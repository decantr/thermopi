#!/usr/bin/python2
import time
import psutil
#from envirophat import weather
from influxdb import InfluxDBClient

# create the db client
db = InfluxDBClient(host='localhost', database='test')

while True:
    # build the json to send to db
    msg = [{
		'measurement': 'temperature',
        'fields': {
			'value': psutil.cpu_percent()
			# 'value' : weather.temperature()
    }}]
    # write to db
    db.write_points(msg)
    # wait before next data point
    time.sleep(1)
