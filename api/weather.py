#!/usr/bin/env python

import pywapi
import string

__all__ = ['Weather']

class Weather:
	
	def __init__(self, location):
		self.location = location
	
	def fetch(self):
		return pywapi.get_weather_from_google(self.location)