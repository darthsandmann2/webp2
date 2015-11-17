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
## Verzeichnisverwaltung
## --------------------------------------------------------------------##
	def erstellen_themavz_db(self, thema):
		pfad = os.path.join('data', thema)
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
		##
		##i = 0
		##for f in os.listdir(pfad):
		##	if os.path.isdir(os.path.join(pfad, f))
		##		thema_dict[i] = f
		##		thema_dict['Anzahl'] = i
		##		i = i+1
		##
		##if os.path.isfile('data/thema.json'):
		##	datei = open(os.path.join('data', 'thema.json'), 'r+')
		##	thema_var = datei.read()
		##	thema_dict = json.loads(thema_var)
		##	anzahl = thema_dict['Anzahl']
		##	thema_dict[anzahl+1] = thema
		##	datei.seek(0)
		##	datei.write(json.dumps(thema_dict, indent=3, ensure_ascii=True))
		##	datei.close
		##else:
		##	thema_dict['Anzahl'] = 1
		##	thema_dict['1'] = thema
		##	datei = codecs.open(os.path.join('data', 'thema.json'), 'w', 'utf-8')
		##	datei.write(json.dumps(thema_dict, indent=3, ensure_ascii=True))
		
	def lesen_themavz_db(self):
		##datei = open(os.path.join('data', 'thema.json'), 'r+')
		##if os.path.isfile('data/thema.json'):
		##	datei = codecs.open(os.path.join('data', 'thema.json'), 'rU', 'utf-8')
		##	thema_var = datei.read()
		##	datei.close()
		##	thema = json.loads(thema_var)
		##	return thema	
		##else:
		##	return 0
		thema_dict = {}
		pfad = os.path.join('data')
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
		
		i = 1
		for f in os.listdir(pfad):
			if os.path.isdir(os.path.join(pfad, f)):
				thema_dict['Anzahl'] = i
				thema_dict[i] = f
				i = i+1
		print (thema_dict)
		return thema_dict

	def erstellen_diskussionvz_db(self, thema, diskussion, user):
		pfad = os.path.join('data', thema)
		mkdir(diskussion)
		##datei = open(os.path.join('data', thema, 'diskussion.json'), 'r+')
		datei = codecs.open(os.path.join('data', thema, 'diskussion.json'), 'rU', 'utf-8')
		diskussion_var = datei.read()
		diskussion_var2 = json.loads(diskussion_var)
		diskussion_var2.update = diskussion
		datei.seek(0)
		datei.write(diskussion_var2)
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
		
#EOF