# coding: utf-8
# id -> 
# id_s -> einlesen aus datei

import cherrypy
from app import datenbank
from app import anzeigen

class programm(object):
	def __init__(self):
		self.datenbank_py = datenbank.datenbank_db()
		self.anzeigen_py = anzeigen.anzeigen_az()
		
	def index(self):
		return self.erzeugen_anzeigen_app()
			
	index.exposed = True
	
	def hinzufuegen_app(self):
		return self.erzeugen_bearbeiten_app()
	
	hinzufuegen_app.exposed = True
	
	def passwort_app(self, id):
		return self.erzeugen_passwort_app(id)
	
	passwort_app.exposed = True
	
	def passwort_loeschen_app(self, id):
		return self.erzeugen_passwort_loeschen_app(id)
	
	passwort_loeschen_app.exposed = True
	
	def bearbeiten_app(self, id_s, pw):
		inhalt_alle = self.datenbank_py.lesen_json_db(id_s)
		if pw == inhalt_alle['Passwort']:
			return self.erzeugen_bearbeiten_app(id_s)
		elif pw == "" or pw != inhalt_alle['Passwort']:
			return self.erzeugen_anzeigen_app()
	bearbeiten_app.exposed = True
	
	# ** damit die übergebene Variable beliebig groß sein kannst, ansonsten würde py nur "Vorname" kennen
	def speichern_app(self, **inhalt_person):
		id_s = inhalt_person["id_s"]
		inhalt_alle = {
			'Vorname': inhalt_person["Vorname_s"],
			'Nachname': inhalt_person["Nachname_s"],
			'Gaeste': inhalt_person["Gaeste_s"],
			'Studiengang': inhalt_person["Studiengang_s"],
			'Betreuer': inhalt_person["Betreuer_s"],
			'Passwort': inhalt_person["Passwort_s"],
			'Matrikelnummer': inhalt_person["Matrikelnummer_s"]
		}
		if id_s != "None":
			self.datenbank_py.update_json_db(id_s, inhalt_alle)
		else:
			id_s = self.datenbank_py.erzeugen_json_db(inhalt_alle)
		return self.anzeigen_py.erzeugen_bearbeiten_az(id_s, inhalt_alle)
	
	speichern_app.exposed = True
	
	def loeschen_app(self, id_s, pw):
		inhalt_alle = self.datenbank_py.lesen_json_db(id_s)
		if pw == inhalt_alle['Passwort']:
			self.datenbank_py.loesche_json_db(id_s)
			return self.erzeugen_anzeigen_app()
		elif pw =="" or pw!= inhalt_alle['Passwort']:
			return self.erzeugen_anzeigen_app()
	
	loeschen_app.exposed = True
	
	def fehler_app(self, *arguments, **kwargs):
		msg_s = "Fehler: " + \
			str(arguments) + \
			' ' + \
			str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)
	
	fehler_app.exposed = True
	
	def erzeugen_anzeigen_app(self):
		inhalt_alle = self.datenbank_py.lesen_json_db()
		return self.anzeigen_py.erzeugen_anzeigen_az(inhalt_alle)
		
	def erzeugen_bearbeiten_app(self, id = None):
		if id != None:
			inhalt_alle = self.datenbank_py.lesen_json_db(id)
		else:
			inhalt_alle = self.datenbank_py.inhalt_db()
		return self.anzeigen_py.erzeugen_bearbeiten_az(id, inhalt_alle)
		
	def erzeugen_passwort_app(self, id):
		inhalt_alle = self.datenbank_py.lesen_json_db(id)
		return self.anzeigen_py.passwort_az(id, inhalt_alle)
		
	def erzeugen_passwort_loeschen_app(self, id):
		inhalt_alle = self.datenbank_py.lesen_json_db(id)
		return self.anzeigen_py.passwort_loeschen_az(id, inhalt_alle)
			
#EOF