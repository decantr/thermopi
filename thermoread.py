#!/usr/bin/python3
import time
from envirophat import weather
from influxdb import InfluxDBClient

# create the db client
client = InfluxDBClient("localhost", 8086, "root", "root", "templog")

while True:
    # build the json to send to db
    json_body = [{
		"measurement": "temperature",
        "fields": {
            "value" : weather.temperature()
    }}]
    # write to db
    client.write_points(json_body)
    # wait before next data point
    time.sleep(1)
