#!/usr/bin/env python

from optparse import OptionParser

import time
import sys

from api.calendar import *
from api.voice import *
from api.weather import *

def main():
	parser = OptionParser()
	parser.add_option("-u", "--username", help="google username")
	parser.add_option("-p", "--password", help="google password")
	parser.add_option("-w", "--weather", help="weather code, zip code, or location.  i.e. Seattle,Washinton or Okinawa,Okinawa,Japan")
	parser.add_option("-n", "--name", help="name you wish to be addressed as.  defauts to 'Master'")

	(options, args) = parser.parse_args()

	if options.weather == None or options.username == None or options.password == None:
		parser.error("incorrect arguments.  requires -u, -p, and -w")

	w = Weather(options.weather)
	c = Calendar('%s@gmail.com' % options.username, options.password)
	v = Voice()

	master = "Master"
	if options.name != None:
		master = options.name

	v.say("Good morning, %s." % master)

	time.sleep(1.0)

	weather = w.fetch()
	weather_say = "Today's weather is. %s degrees Celcius. %s. condition. %s"
	temp_c = weather['current_conditions']['temp_c']
	humidity = weather['current_conditions']['humidity']
	condition = weather['current_conditions']['condition']
	v.say(weather_say % (temp_c, humidity, condition))

	time.sleep(1.0)

	calendar_events = c.fetch()
	v.say("Today's events are as follows.")
	time.sleep(1.0)
	calendar_say = "%s. From. %s:%s. to. %s:%s."
	if len(calendar_events) == 0:
		v.say("No events scheduled.")
	else:	
		for event in calendar_events:
			v.say(calendar_say % (event[0], event[1][11:13], event[1][14:16], event[2][11:13], event[2][14:16]))
			time.sleep(1.0)
			
if __name__ == "__main__":
    main()
