#!/usr/bin/env python

import webapp2

class ScoutingData(webapp2.RequestHandler):
	def get(self, team_key, event_key, match_key):
		self.response.write('Called /2014/ScoutingData/%s/%s/%s' % (team_key, event_key, match_key))
