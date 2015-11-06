# coding: utf-8

import cherrypy
from app import datenbank
from app import anzeigen

class programm(object):
## --------------------------------------------------------------------##
	def __init__(self):
		self.datenbank_py = datenbank.datenbank_db()
		self.anzeigen_py = anzeigen.anzeigen_az()
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##	
## Startseite erzeugen und anzeigen
## --------------------------------------------------------------------##	
	def index(self):
		return self.erzeugen_anzeigen_app()
		
	index.exposed = True
	
	
	def erzeugen_anzeigen_app(self):
		content = self.datenbank_py.lesen_json_db()
		return self.anzeigen_py.erzeugen_anzeigen_az(content)
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Fehlerausgabe
## --------------------------------------------------------------------##
	def fehler_app(self, *arguments, **kwargs):
		msg_s = "Fehler: " + \
			str(arguments) + \
			' ' + \
			str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)
	
	fehler_app.exposed = True
## --------------------------------------------------------------------##
	
	
	
#EOF