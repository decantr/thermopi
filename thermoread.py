#!/usr/bin/python3
from influxdb import InfluxDBClient
from psutil import cpu_percent
#from envirophat import weather

# create the db client
db = InfluxDBClient(host='localhost', database='test')

# build the json to send to db
msg = [{
	'measurement': 'temperature',
    'fields': {
		# 'value' : weather.temperature()
		'value': cpu_percent()
}}]
# write to db
db.write_points(msg)
# wait before next data point
