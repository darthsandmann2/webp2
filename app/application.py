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
		return self.erzeugen_index_app()
	index.exposed = True
	
	def foren(self):
		return self.erzeugen_foren_app()
	foren.exposed = True
	
	def themen(self, thema):
		return self.erzeugen_themen_app(thema)
	themen.exposed = True
	
	def themen_neu(self, thema):
		return self.content_themen_neu_app(thema)
	themen_neu.exposed = True
	
	def themen_loeschen(self, **content):
		thema = content["thema"]
		return self.content_themen_loeschen_app(thema)
	themen_loeschen.exposed = True
	
	def beitrag_loeschen(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		beitrag = content["beitrag"]
		return self.content_beitrag_loeschen_app(thema, diskussion, beitrag)
	beitrag_loeschen.exposed = True
	
	def diskussion_neu(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		username = content["username"]
		inhalt = content["inhalt"]
		return self.content_diskussion_neu_app(thema, diskussion, username, inhalt)
	diskussion_neu.exposed = True
	
	def diskussion_loeschen(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		return self.content_diskussion_loeschen_app(thema, diskussion)
	diskussion_loeschen.exposed = True
	
	def beitraege(self, thema, diskussion):
		return self.erzeugen_beitraege_app(thema, diskussion)
	beitraege.exposed = True
		
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Webpages verarbeiten
## --------------------------------------------------------------------##
	def erzeugen_index_app(self):
		content = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_index_az(content)
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
		
	def content_themen_loeschen_app(self, thema):
		self.datenbank_py.loeschen_themavz_db(thema)
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)

	def content_diskussion_neu_app(self, thema, diskussion, username, inhalt):
		self.datenbank_py.erstellen_diskussionvz_db(thema, diskussion)
		self.datenbank_py.erstellen_beitrag_db(thema, diskussion, username, inhalt)
		content = self.datenbank_py.lesen_beitraege_db(thema, diskussion)
		return self.anzeigen_py.erzeugen_beitraege_az(content)
	
	def content_diskussion_loeschen_app(self, thema, diskussion):
		self.datenbank_py.loeschen_diskussionvz_db(thema, diskussion)
		content = self.datenbank_py.lesen_diskussionvz_db(thema)
		return self.anzeigen_py.erzeugen_themen_az(content)		
	
	def content_beitrag_loeschen_app(self, thema, diskussion, beitrag):
		self.datenbank_py.loeschen_beitrag_db(thema, diskussion, beitrag)
		content = self.datenbank_py.lesen_beitraege_db(thema, diskussion)
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
