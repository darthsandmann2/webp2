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
	## Userverwaltung
	def index(self):
		return self.erzeugen_foren_app()
	index.exposed = True
	
	def login(self, **content):
		user = content['username']
		passwort = content['passwort']
		return self.content_passwort(user, passwort)
	login.exposed = True
	
	def user_neu(self, **content):
		user = content['username']
		passwort = content['passwort']
		return self.content_user_neu(user, passwort)
	user_neu.exposed = True
		
	def user_bearbeiten(self, **content):
		user = content['username']
		rolle = content['rolle']
		passwort = content['passwort']
		return self.content_user_bearbeiten(user, rolle, passwort)
	user_bearbeiten.exposed = True
	
	def user_loeschen(self, id):
		return self.content_user_loeschen_app(id)
	user_loeschen.exposed = True
	
	## Themen
	def account(self):
		return self.erzeugen_account_app()
	account.exposed = True
	
	def themen(self, thema):
		return self.erzeugen_themen_app(thema)
	themen.exposed = True
	
	def themen_neu(self, **content):
		username = content["username"]
		passwort = content["passwort"]
		thema = content["thema"]
		return self.content_themen_neu_app(username, passwort, thema)
	themen_neu.exposed = True
	
	def themen_loeschen(self, **content):
		thema = content["thema"]
		return self.content_themen_loeschen_app(thema)
	themen_loeschen.exposed = True
	
	## Diskussion
	def beitraege(self, thema, diskussion):
		return self.erzeugen_beitraege_app(thema, diskussion)
	beitraege.exposed = True
	
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
		passwort = content["passwort"]
		inhalt = content["inhalt"]
		return self.content_diskussion_neu_app(thema, diskussion, username, passwort, inhalt)
	diskussion_neu.exposed = True
	
	def diskussion_loeschen(self, **content):
		thema = content["thema"]
		diskussion = content["diskussion"]
		return self.content_diskussion_loeschen_app(thema, diskussion)
	diskussion_loeschen.exposed = True
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Webpages verarbeiten
## --------------------------------------------------------------------##
	def erzeugen_account_app(self):
		user = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_account_az(user)
		
	def erzeugen_user_app(self, username_var):
		user = self.datenbank_py.lesen_user_db()
		print(user[username_var])
		return self.anzeigen_py.erzeugen_user_az(user[username_var])
		
	def erzeugen_admin_app(self):
		user = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_admin_az(user)
		
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
	## Passwörter
	def passwort_check(self, username_var, passwort_var):
		user = self.datenbank_py.lesen_user_db()
		if not user.get(username_var) == None:
			if passwort_var == user[username_var]['Passwort']:
				return 1
			else:
				return 0
		else:
			return 0
	
	def passwort_check_admin(self, username_var, passwort_var):
		user = self.datenbank_py.lesen_user_db()
		if not user.get(username_var) == None:
			if passwort_var == user[username_var]['Passwort']:
				if user[username_var]['Rolle'] == '1':
					return 1
				else:
					return 2
			else:
				return 0
		else:
			return 0
	
	def content_passwort(self, username_var, passwort_var):
		check = self.passwort_check_admin(username_var, passwort_var)
		if check == 1:
			return self.erzeugen_admin_app()
		if check == 2:
			return self.erzeugen_user_app(username_var)
		if check == 0:
			return self.erzeugen_account_app()
			
	def content_passwort_admin(self, username_var, passwort_var):
		check = self.passwort_check_admin(username_var, passwort_var)
		if check == 1:
			return self.erzeugen_admin_app()
		else:
			return self.erzeugen_account_app()
			
	def content_passwort_user(self, username_var, passwort_var):
		check = self.passwort_check(username_var, passwort_var)
		if check == 1:
			return self.erzeugen_user_app(username_var)
		else:
			return self.erzeugen_account_app()

	## User
	def content_user_neu(self, user, passwort):
		self.datenbank_py.erstellen_user_db(user, passwort)
		user = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_account_az(user)
		
	def content_user_bearbeiten(self, user, rolle, passwort):
		self.datenbank_py.update_user_db(user, rolle, passwort)
		user = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_index_az(user)
		
	def content_user_loeschen_app(self, id):
		self.datenbank_py.loeschen_user_db(id)
		user = self.datenbank_py.lesen_user_db()
		return self.anzeigen_py.erzeugen_index_az(user)
	
	## Themen
	def content_themen_neu_app(self, username_var, passwort_var, thema):
		check = self.passwort_check_admin(username_var, passwort_var)
		if check == 1:
			self.datenbank_py.erstellen_themavz_db(thema)
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)
		
	def content_themen_loeschen_app(self, thema):
		self.datenbank_py.loeschen_themavz_db(thema)
		content = self.datenbank_py.lesen_themavz_db()
		return self.anzeigen_py.erzeugen_foren_az(content)
	
	## Diskussion
	def content_diskussion_neu_app(self, thema, diskussion, username_var, passwort_var, inhalt):
		check = self.passwort_check(username_var, passwort_var)
		if check == 1:
			self.datenbank_py.erstellen_diskussionvz_db(thema, diskussion)
			self.datenbank_py.erstellen_beitrag_db(thema, diskussion, username_var, inhalt)
			content = self.datenbank_py.lesen_beitraege_db(thema, diskussion)
			return self.anzeigen_py.erzeugen_beitraege_az(content)
		else:
			content = self.datenbank_py.lesen_diskussionvz_db(thema)
			return self.anzeigen_py.erzeugen_themen_az(content)	

	def content_diskussion_loeschen_app(self, thema, diskussion):
		self.datenbank_py.loeschen_diskussionvz_db(thema, diskussion)
		content = self.datenbank_py.lesen_diskussionvz_db(thema)
		return self.anzeigen_py.erzeugen_themen_az(content)		
	
	def content_beitrag_loeschen_app(self, thema, diskussion, beitrag):
		self.datenbank_py.loeschen_beitrag_db(thema, diskussion, beitrag)
		content = self.datenbank_py.lesen_beitraege_db(thema, diskussion)
		return self.anzeigen_py.erzeugen_beitraege_az(content)
## --------------------------------------------------------------------##
#EOF
