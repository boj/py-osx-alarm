#!/usr/bin/env python

import subprocess

__all__ = ['Voice']

class Voice:
	
	def __init__(self, voice="Vicki"):
		self.voice = voice
	
	def say(self, text):
		subprocess.call(['say', "-v%s" % self.voice, text])