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


	def themen(self, thema):
		return self.erzeugen_themen_app(thema)
	themen.exposed = True


	def beitraege(self, thema, diskussion):
		return self.erzeugen_beitraege_app(thema, diskussion)
	beitraege.exposed = True
	
	def themen_neu(self, thema):
		return self.content_themen_neu_app(thema)
	themen_neu.exposed = True
	
	def diskussion_neu(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		return self.content_diskussion_neu_app(thema, diskussion)
	diskussion_neu.exposed = True
	
	def themen_loeschen(self, thema):
		return self.content_themen_loeschen_app(thema)
	themen_loeschen.exposed = True
	
	def diskussion_loeschen(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		return self.content_diskussion_loeschen_app(thema, diskussion)
	diskussion_loeschen.exposed = True
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Webpages verarbeiten
## --------------------------------------------------------------------##
	def erzeugen_foren_app(self):
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)

	def erzeugen_themen_app(self, thema):
		content = self.datenbank_py.lesen_diskussionvz_db(thema)
		return self.anzeigen_py.erzeugen_themen_az(content)

	def erzeugen_beitraege_app(self, thema, diskussion):
		content = self.datenbank_py.lesen_beitraege_db(thema, diskussion)
		return self.anzeigen_py.erzeugen_beitraege_az(content)
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Content verarbeiten
## --------------------------------------------------------------------##
	def content_themen_neu_app(self, thema):
		self.datenbank_py.erstellen_themavz_db(thema)
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)
		
	def content_diskussion_neu_app(self, thema, diskussion):
		self.datenbank_py.erstellen_diskussionvz_db(thema, diskussion)
		content = self.datenbank_py.lesen_diskussionvz_db(thema)
		return self.anzeigen_py.erzeugen_themen_az(content)
		
	def content_themen_loeschen_app(self, thema):
		self.datenbank_py.loeschen_themavz_db(thema)
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)
		
	def content_diskussion_loeschen_app(self, thema, diskussion):
		self.datenbank_py.loeschen_diskussionvz_db(thema, diskussion)
		content = self.datenbank_py.lesen_diskussionvz_db(thema)
		return self.anzeigen_py.erzeugen_themen_az(content)
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
