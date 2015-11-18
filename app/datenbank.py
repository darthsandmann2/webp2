# coding: utf-8

import os
import os.path
import codecs
import json
import time
import shutil
from collections import OrderedDict


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
			os.mkdir(os.path.join('data'))
		pfad = os.path.join('data')
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
		i = 1
		for f in os.listdir(pfad):
			if os.path.isdir(os.path.join(pfad, f)):
				thema_dict[i] = {}
				j = 0
				thema_dict[i]['thema'] = f
				for f in os.listdir(pfad+'/'+f):
					j = j+1
				thema_dict[i]['eintraege'] = j
				i = i+1
		if i == 1:
			thema_dict[i] = {}
			thema_dict[i]['thema'] = 'keine'
			thema_dict[i]['eintraege'] = 0
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
		return OrderedDict(sorted(diskussion_dict.items(), key=lambda t: t[0]))
## --------------------------------------------------------------------##
		

		
## --------------------------------------------------------------------##
## Verzeichnis verwalten
## --------------------------------------------------------------------##
	def erstellen_themavz_db(self, thema):
		pfad = os.path.join('data')
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data'))
		pfad = os.path.join('data', thema)
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema))
			
	def erstellen_diskussionvz_db(self, thema, diskussion):
		pfad = os.path.join('data', thema, diskussion)
		if not os.path.exists(pfad):
			os.mkdir(os.path.join('data', thema, diskussion))
			
	def loeschen_themavz_db(self, thema):
		pfad = os.path.join('data', thema)
		shutil.rmtree(pfad)
		
	def loeschen_diskussionvz_db(self, thema, diskussion):
		pfad = os.path.join('data', thema, diskussion)
		shutil.rmtree(pfad)
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Diskussionen
## --------------------------------------------------------------------##
	def erstellen_beitrag_db(self, thema, diskussion, username, inhalt):
		id = 0
		id_var = 0
		pfad = os.path.join('data', thema, diskussion)
		zeit = time.strftime("%H:%M:%S")                
		inhalt_json = {
			'username': username,
			'titel': diskussion,
			'inhalt': inhalt,
			'thema': thema,
			'zeit': zeit
		}
		ordner = os.listdir(pfad)
		for dateiname in ordner:
			if dateiname.endswith('.json'):
				id_int = int(dateiname[:-5])
				id_int = id_int + 1
				if id_int > id:
					id = id_int
		id_str = str(id) + '.json'
		datei = codecs.open(os.path.join('data',thema, diskussion, id_str), 'w', 'utf-8')
		datei.write(json.dumps(inhalt_json, indent=3, ensure_ascii=True))
		datei.close()   
	
	def lesen_beitraege_db(self, thema, diskussion):
		beitraege = {}
		beitraege_sorted = {}
		pfad = os.path.join('data', thema, diskussion)
		ordner = os.listdir(pfad)
		for dateiname in ordner:
			if dateiname.endswith('.json'):
				datei = codecs.open(os.path.join('data', thema, diskussion, dateiname), 'r+', 'utf-8')
				id = dateiname[:-5]
				dateiinhalt = datei.read()
				beitraege[id] = json.loads(dateiinhalt)
		return OrderedDict(sorted(beitraege.items(), key=lambda t: t[0]))
		
	def loeschen_beitrag_db(self, thema, diskussion, beitrag):
		pfad = os.path.join('data', thema, diskussion, beitrag+'.json')
		os.remove(pfad)
## --------------------------------------------------------------------##		

#EOF