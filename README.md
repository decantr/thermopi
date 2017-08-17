# thermopi
logs the current temperature read by the enviro phat to a local influxdb.

## setup
1. clone the repo
1. setup crontab entry to run it every minuite
1. set up a influx database called templog
1. add the data source in grafana

## requirements
###### hardware
* rpi zero
* enviro phat

###### software
* python 3
* influxdb (local)
* `python3-envirophat`
* `python3-influxdb`
