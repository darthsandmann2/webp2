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
	def erstellen_diskussion_db(self, thema, diskussion, titel, inhalt):
		# diskussion.json:
		#	vorhandene .json beiträge (id)
		#	username
		#	Bearbeiter
		#	zeitpunkt
		#	titel
		#	inhalt
	
	def lesen_diskussion_db(self, thema, diskussion):
		# diskussion.json auslesen:
		#	welche dateien müssen gelesen werden
		#	erster post
		# weitere posts .json dateien auslesen