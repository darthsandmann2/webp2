# coding: utf-8

import os
import os.path
import codecs
import json

class datenbank_db(object):
	def __init__(self):
		self.inhalt_alle = {}
		self.inhalt_betreuer = {}
		self.lesen_inhalt_db()
		
	def erzeugen_json_db(self, inhalt_person):
		id = self.naechste_db()
		datei = codecs.open(os.path.join('data', id+'.json'), 'w', 'utf-8')
		datei.write(json.dumps(inhalt_person, indent=3, ensure_ascii=True))
		datei.close()
		self.inhalt_alle[id] = inhalt_person
		return id
		
	def lesen_json_db(self, id = None):
		inhalt_alle = None
		if id == None:
			inhalt_alle = self.inhalt_alle
		else:
			if id in self.inhalt_alle:
				inhalt_alle = self.inhalt_alle[id]
		return inhalt_alle
		
	def update_json_db(self, id, inhalt_person):
		status_b = False
		if id in self.inhalt_alle:
			datei = codecs.open(os.path.join('data', id+'.json'), 'w', 'utf-8')
			datei.write(json.dumps(inhalt_person, indent=3, ensure_ascii=True))
			datei.close
			self.inhalt_alle[id] = inhalt_person
			status_b = True
		return status_b
		
	def loesche_json_db(self, id):
		status_b = False
		if id in self.inhalt_alle:
			os.remove(os.path.join('data', id+'.json'))
			del self.inhalt_alle[id]
			status_b = True
		return status_b
		
	def inhalt_db(self):
		return {
			'Vorname': '',
			'Nachname': '',
			'Gaeste': '',
			'Studiengang': '',
			'Betreuer': '',
			'Passwort': '',
			'Matrikelnummer': '',
			'Abschlussarbeit': ''
			}
	
	def lesen_inhalt_db(self):
		ordner = os.listdir('data')
		for dateiname in ordner:
			if dateiname.endswith('.json') and dateiname != 'letztes.json' and dateiname != 'aktuell.json':
				datei = codecs.open(os.path.join('data', dateiname), 'rU', 'utf-8')
				dateiinhalt = datei.read()
				id = dateiname[:-5]
				self.inhalt_alle[id] = json.loads(dateiinhalt)
				
	def naechste_db(self):
		datei = open(os.path.join('data', 'letztes.json'), 'r+')
		letztes = datei.read()
		letztes = str(int(letztes)+1)
		datei.seek(0)
		datei.write(letztes)
		datei.close()
		return letztes
	
	def aktuell_db(self,id):
		datei = open(os.path.join('data', 'aktuell.json'), 'r+')
		datei.seek(0)
		datei.write(id)
		datei.close()
	

	def lesen_aktuell_db(self,id):
		datei = open(os.path.join('data', 'aktuell.json'), 'r+')
		aktuell_id = datei.read()
		datei.close()
		return aktuell_id  
# EOF