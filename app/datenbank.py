# coding: utf-8

import os
import os.path
import codecs
import json
import time


class datenbank_db(object):
## --------------------------------------------------------------------##
	def __init__(self):
		self.thema_dict = {}
		self.lesen_themavz_db()
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Verzeichnis auslesen
## --------------------------------------------------------------------##
	def lesen_themavz_db(self):
		thema_dict = {}
		pfad = os.path.join('data')
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
		i = 1
		for f in os.listdir(pfad):
			if os.path.isdir(os.path.join(pfad, f)):
				thema_dict[i] = f
				i = i+1
		print (thema_dict)
		return thema_dict
			
	def lesen_diskussionvz_db(self, thema):
		diskussion_dict = {}
		pfad = os.path.join('data', thema)
		i = 1
		for f in os.listdir(pfad):
			if os.path.isdir(os.path.join(pfad, f)):
				diskussion_dict[f] = {}
				diskussion_dict[f]['Diskussion'] = f
				diskussion_dict[f]['Thema'] = thema
				i = i+1
		if i == 1:
			diskussion_dict['keine'] = {}
			diskussion_dict['keine']['Thema'] = thema
			diskussion_dict['keine']['Diskussion'] = "keine"
		print (diskussion_dict)
		return diskussion_dict
## --------------------------------------------------------------------##
		

		
## --------------------------------------------------------------------##
## Verzeichnis verwalten
## --------------------------------------------------------------------##
	def erstellen_themavz_db(self, thema):
		pfad = os.path.join('data', thema)
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
			
	def erstellen_diskussionvz_db(self, thema, diskussion):
		pfad = os.path.join('data', thema, diskussion)
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema, diskussion))
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Diskussionen
## --------------------------------------------------------------------##
	def erstellen_hauptbeitrag_db(self, thema, diskussion, titel, inhalt, username):
		# diskussion.json:
		#	vorhandene .json beitraege (id)
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
		#       beitraege aus Beitrag 1 auslesen und neuen Eintrag hinzufuegen                
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
		#	welche dateien muessen gelesen werden
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
## --------------------------------------------------------------------##		
#EOF