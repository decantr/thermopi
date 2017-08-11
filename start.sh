#!/bin/bash
pid=$(pgrep thermoread.py)

if [ -z $pid ]; then
	$(/usr/bin/python3 thermoread)
fi
