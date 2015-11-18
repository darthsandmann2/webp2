# coding: utf-8

import os.path
from mako.template import Template
from mako.lookup import TemplateLookup


class anzeigen_az(object):
## --------------------------------------------------------------------##
## Festlegen des Pfades für die Templates
## --------------------------------------------------------------------##
	def __init__(self):
		self.path_s = 'template'
		self.lookup_o = TemplateLookup(directories=['/'])
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Rendern der Internetseite
## --------------------------------------------------------------------##
	def erzeugen_az(self, template_praktikum, content_var):
		template_praktikum = Template(filename=os.path.join(self.path_s, template_praktikum), output_encoding='utf-8', lookup=self.lookup_o)
		return template_praktikum.render(content = content_var)
## --------------------------------------------------------------------##



## --------------------------------------------------------------------##
## Übergabe der Templates an den Renderer
## --------------------------------------------------------------------##	
	def erzeugen_index_az(self, content_var):
		return self.erzeugen_az('index.html', content_var)
		
	def erzeugen_admin_az(self, content_var):
		return self.erzeugen_az('admin.html', content_var)
		
	def erzeugen_foren_az(self, content_var):
		return self.erzeugen_az('foren.html', content_var)
		
	def erzeugen_themen_az(self, content_var):
		return self.erzeugen_az('themen.html', content_var)
		
	def erzeugen_beitraege_az(self, content_var):
		return self.erzeugen_az('beitraege.html', content_var)
## --------------------------------------------------------------------##

#EOF