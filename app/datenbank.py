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
## Verzeichnisverwaltung
## --------------------------------------------------------------------##
	def erstellen_themavz_db(self, thema):
		mkdir(verzeichnis)
		datei = open(os.path.join('data', 'thema.json'), 'r+')
		thema_var = datei.read()
		thema_var.update = thema
		datei.seek()
		datei.write(thema_var)
		datei.close
		
	def lesen_themavz_db(self):
		datei = open(os.path.join('data', 'thema.json'), 'r+')
		thema = datei.read()
		datei.close()
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
	def erstellen_diskussion_db(self, thema, diskussion, titel, inhalt, username):
		# diskussion.json:
		#	vorhandene .json beiträge (id)
		#	username
		#	Bearbeiter
		#	zeitpunkt
		#	titel
		#	inhalt
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
                inhalt_json = {
			'username': username,
			'inhalt': inhalt,
			'thema': thema,
			'diskussion': diskussion,
			'zeit': zeit
		}
                datei = codecs.open(os.path.join('data',thema, diskussion, beitrag+'.json'), 'w', 'utf-8')
                datei.write(inhalt_json)    
	
        def lesen_diskussion_db(self, thema, diskussion):
		# diskussion.json auslesen:
		#	welche dateien müssen gelesen werden
        	#	erster post
		# weitere posts .json dateien auslesen
                datei = open(os.path.join('data', thema, diskussion, '1.json'), 'r+')
                temp = datei.read()
                beitraege = temp[beitraege] // ?
                for i in beitraege:
                        ausgabe[i] = lesen.beitrag(beitraege[i])
                return ausgabe

        def lesen_beitrag_db(self, thema, diskussion, beitrag):
                datei = open(os.path.join('data', thema, diskussion, '1.json'), 'r+')
                temp = datei.read()
                return temp
