# coding: utf-8

import os
import os.path
import codecs
import json
import time


class datenbank_db(object):
## --------------------------------------------------------------------##
	def __init__(self):
		self.lesen_themavz_db()
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Verzeichnisverwaltung
## --------------------------------------------------------------------##
	def erstellen_themavz_db(self, thema):
		mkdir(verzeichnis)
		datei = open(os.path.join('data', 'thema.json'), 'r+')
		thema_var = datei.read()
		if thema_var == None:
			datei.write(thema)
		else:
			thema_var.update = thema
			datei.seek()
			datei.write(thema_var)
		datei.close
		
	def lesen_themavz_db(self):
		##datei = open(os.path.join('data', 'thema.json'), 'r+')
		os.path.isfile('data', 'thema.json')
		datei = codecs.open(os.path.join('data', 'thema.json'), 'rU', 'utf-8')
		thema_var = datei.read()
		datei.close()
		thema = json.loads(thema_var)
		return thema	

	def erstellen_diskussionvz_db(self, thema, diskussion, user):
		pfad = path.join('data', thema)
		mkdir(diskussion)
		datei = open(os.path.join('data', thema, 'diskussion.json'), 'r+')
		diskussion_var = datei.read()
		diskussion_var.update = diskussion
		datei.seek()
		datei.write(diskussion_var)
		datei.close
			
	def lesen_diskussionvz_db(self, thema):
		datei = open(os.path.join('data', thema, 'thema.json'), 'r+')
		themen = datei.read()
		datei.close()
		return diskussion
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Diskussionen
## --------------------------------------------------------------------##
	def erstellen_hauptbeitrag_db(self, thema, diskussion, titel, inhalt, username):
		# diskussion.json:
		#	vorhandene .json beitr�ge (id)
		#	username
		#	Bearbeiter
		#	zeitpunkt
		#	titel
		#	inhalt
		zeit = time.strftime("%H:%M:%S")               
		inhalt_json = {
			'username': username,
			'inhalt': inhalt,
			'thema': thema,
			'diskussion': diskussion,
			'zeit': zeit,
			'beitraege': {}
			}
		datei = codecs.open(os.path.join('data',thema, diskussion, '1.json'), 'w', 'utf-8')
		datei.write(json.dumps(inhalt_json, indent=3, ensure_ascii=True))
		datei.close()

	def erstellen_beitrag_db(self, thema, diskussion, titel, inhalt, username):       
		# Fehlt:
		#       beitr�ge aus Beitrag 1 auslesen und neuen Eintrag hinzuf�gen                
		zeit = time.strftime("%H:%M:%S")                
		inhalt_json = {
			'username': username,
			'inhalt': inhalt,
			'thema': thema,
			'diskussion': diskussion,
			'zeit': zeit
		}
		datei = codecs.open(os.path.join('data',thema, diskussion, beitrag+'.json'), 'w', 'utf-8')
		datei.write(inhalt_json)    
	
	def lesen_beitraege_db(self, thema, diskussion):
		# diskussion.json auslesen:
		#	welche dateien m�ssen gelesen werden
		#	erster post
		# weitere posts .json dateien auslesen
		datei = open(os.path.join('data', thema, diskussion, '1.json'), 'r+')
		temp = datei.read()
		beitraege = temp["beitraege"] ## ??
		for i in beitraege:
			ausgabe[i] = lesen.beitrag(beitraege[i])
		return ausgabe

	def lesen_beitrag_db(self, thema, diskussion, beitrag):
		datei = open(os.path.join('data', thema, diskussion, '1.json'), 'r+')
		temp = datei.read()
		return temp
		
#EOF