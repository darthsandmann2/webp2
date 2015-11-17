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
## Zugriffe
## --------------------------------------------------------------------##
	def index(self):
		return self.erzeugen_foren_app()
	index.exposed = True


	def themen(self, id):
		return self.erzeugen_themen_app(id)
	themen.exposed = True


	def beitraege(self, id):
		return self.erzeugen_beitraege_app()
	themen.exposed = True
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Webpages verarbeiten
## --------------------------------------------------------------------##
	def erzeugen_foren_app(self):
		## testerzeugung
		self.datenbank_py.erstellen_themavz_db("test1")
		self.datenbank_py.erstellen_themavz_db("test2")
		self.datenbank_py.erstellen_themavz_db("test3")
		self.datenbank_py.erstellen_diskussionvz_db("test1", "beitrag1")
		self.datenbank_py.erstellen_diskussionvz_db("test1", "beitrag2")
		self.datenbank_py.erstellen_diskussionvz_db("test1", "beitrag3")
		self.datenbank_py.erstellen_diskussionvz_db("test3", "beitrag1")
		self.datenbank_py.erstellen_diskussionvz_db("test3", "beitrag2")
		self.datenbank_py.erstellen_diskussionvz_db("test2", "beitrag1")
		self.datenbank_py.erstellen_diskussionvz_db("test2", "beitrag2")
		## ----------- ##
		
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)

	def erzeugen_themen_app(self, id):
		content = self.datenbank_py.lesen_diskussionvz_db(id)
		return self.anzeigen_py.erzeugen_themen_az(content)

	def erzeugen_beitraege_app(self):
		content = self.datenbank_py.lesen_beitraege_db()
		return self.anzeigen_py.erzeugen_beitraege_az(content)
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
