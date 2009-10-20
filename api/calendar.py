#!/usr/bin/env python

try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import gdata.calendar.service
import gdata.service
import gdata.calendar
import operator
import time
import datetime

__all__ = ['Calendar']

class Calendar:
	
	def __init__(self, username, password):
		self.client = gdata.calendar.service.CalendarService()
		self.client.ClientLogin(username, password)

	def fetch(self):
		events = []
		query = gdata.calendar.service.CalendarEventQuery('default', 'private', 'full')
		query.start_min = str(datetime.date.today())
		query.start_max = str(datetime.date.today() + datetime.timedelta(days=1))
		feed = self.client.CalendarQuery(query)
		for i, an_event in enumerate(feed.entry):
			events.append(
				(
					an_event.title.text,
					an_event.when[0].start_time,
					an_event.when[0].end_time
				)
			)
		events = sorted(events, key=operator.itemgetter(1))
		return events	
