from mako import exceptions
from mako.template import Template
from mako.lookup import TemplateLookup

class view( object ):
	def index( self ):
		try:
			index_template = Template(filename='./content/index.txt')
			return index_template.render()
		except:
			return exceptions.html_error_template().render()

	def registration_form( self ):
		try:
			registration_form_template = Template(filename='./content/registration_form.txt')
			return registration_form_template.render()
		except:
			return exceptions.html_error_template().render()

	def password_form( self, ident ):
		try:
			password_form_template = Template(filename='./content/password_form.txt')
			return password_form_template.render( ident )
		except:
			return exceptions.html_error_template().render()

	def edit_form( self, ident ):
		try:
			edit_form_template = Template(filename='./content/edit_form.txt')
			return edit_form_template.render( ID=ident )
		except:
			return exceptions.html_error_template().render()

	def error_page( self, msg ):
		try:
			error_page_template = Template(filename='./content/error_page.txt')
			return error_page_template.render( MSG=msg )
		except:
			return exceptions.html_error_template().render()