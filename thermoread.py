#!/usr/bin/python3
import time
import sys
import datetime
from influxdb import InfluxDBClient
import envirohat

# create the db client
client = InfluxDBClient("localhost", "8086", "root", "root", "templog")

while True:
    # build the json to send to db
    json_body = [{
        "fields": {
            "temperature" : envirohat.weather.temperature()
    }}]
    # write to db
    client.write_points(json_body)
    # wait before next data point
    time.sleep(1)
