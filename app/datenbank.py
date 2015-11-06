# coding: utf-8

import os
import os.path
import codecs
import json


class datenbank_db(object):
## --------------------------------------------------------------------##
	def __init__(self):
		self.content = {}
		self.user = {}
		self.lesen_content_db()
		self.lesen_user_db()
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Json Dateien einlesen
## --------------------------------------------------------------------##
	def lesen_content_db(self):
		ordner = os.listdir('data')
		datei = codecs.open(os.path.join('data', 'content.json'), 'rU', 'utf-8')
		dateiinhalt = datei.read()
		self.content = json.loads(dateiinhalt)
		
	def lesen_user_db(self):
		ordner = os.listdir('data')
		datei = codecs.open(os.path.join('data', 'user.json'), 'rU', 'utf-8')
		dateiinhalt = datei.read()
		self.content = json.loads(dateiinhalt)
## --------------------------------------------------------------------##