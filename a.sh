#!/bin/sh
pid=$(pgrep a.py)

if (-z $pid); then
	$(/bin/bash /home/r2sadmin/a.py)
