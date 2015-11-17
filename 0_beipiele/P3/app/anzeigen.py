# coding: utf-8

import os.path

from mako.template import Template
from mako.lookup import TemplateLookup

class anzeigen_az(object):
	def __init__(self):
		self.path_s = 'template'
		self.lookup_o = TemplateLookup(directories=['/'])

	def erzeugen_az(self, template_praktikum, inhalt_person):
		template_praktikum = Template(filename=os.path.join(self.path_s, template_praktikum), output_encoding='utf-8', lookup=self.lookup_o)
		return template_praktikum.render(inhalt_alle = inhalt_person)
	
	def erzeugen_anzeigen_az(self, inhalt_person):
		return self.erzeugen_az('anzeigen.html', inhalt_person)
		
	def erzeugen_anzeigen_ausschuss_az(self, inhalt_person):
		return self.erzeugen_az('ausschuss.html', inhalt_person)
		
	def erzeugen_bearbeiten_az(self, id, inhalt_person):
		inhalt_person['id'] = id
		return self.erzeugen_az('bearbeiten.html', inhalt_person)
		
	def erzeugen_bearbeiten_ausschuss_az(self, id, inhalt_person):
		inhalt_person['id'] = id
		return self.erzeugen_az('bearbeiten_ausschuss.html', inhalt_person)
	
	def passwort_az(self, id, inhalt_person):
		inhalt_person['id'] = id
		return self.erzeugen_az('passwort.html', inhalt_person)
	
	def passwort_loeschen_az(self, id, inhalt_person):
		inhalt_person['id'] = id
		return self.erzeugen_az('passwort_loeschen.html', inhalt_person)
		
	def weiterleiten_az(self, id, inhalt_person):
		inhalt_person['id'] = id
		return self.erzeugen_az('weiterleiten.js', inhalt_person)
#EOF