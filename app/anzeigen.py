import os.path

from mako.template import Template
from mako.lookup import TemplateLookup


class anzeigen_az(object):
	def __init__(self):
		self.path_s = 'template'
		self.lookup_o = TemplateLookup(directories=['/'])
		
		
		
	def erzeugen_az(self, template_praktikum, content_var):
		template_praktikum = Template(filename=os.path.join(self.path_s, template_praktikum), output_encoding='utf-8', lookup=self.lookup_o)
		return template_praktikum.render(content = content_var)
		
	
	def erzeugen_anzeigen_az(self, content_var):
		return self.erzeugen_az('anzeigen.html', content_var)
		
#EOF