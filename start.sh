#!/bin/sh
pid=$(pgrep thermoread.py)

if (-z $pid); then
	$(/bin/bash /home/r2sadmin/thermoread.py)
