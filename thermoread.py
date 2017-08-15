#!/usr/bin/python3
from time import sleep
from influxdb import InfluxDBClient
from tendo import singleton

# make sure there is no other process running
i = singleton.SingleInstance()

# create the db client
db = InfluxDBClient(host='localhost', database='test')

while True:
    # build the json to send to db
    msg = [{
		'measurement': 'temperature',
        'fields': {
			'value' : weather.temperature()
    }}]
    # write to db
    db.write_points(msg)
    # wait before next data point
    sleep(1)
