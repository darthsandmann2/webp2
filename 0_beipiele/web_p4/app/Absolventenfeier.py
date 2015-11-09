import cherrypy
import json
import os
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from app import view
from app import account

class Absolventenfeier_cl( object ):

	def __init__( self ):
		self._view = view.view()
		self._account = account.Account()

	@cherrypy.expose
	def index( self ):
		return self._view.index()

	@cherrypy.expose
	def registration_form( self ):
		return self._view.registration_form()

	@cherrypy.expose
	def edit_form( self, ident = -1 ):
		return self._view.edit_form( ident )

	@cherrypy.expose
	def save( self, **form_input ):
		if( not form_input.get( 'ID' ) ):
			self._account.registration( **form_input )
		else:
			if( not self._account.edit( **form_input ) ):
				return self._view.error_page( "Die Eingabe war fehlerhaft!" )
		return self._view.index()

	@cherrypy.expose
	def default(self, *arglist, **kwargs):
		msg_s = "unbekannte Anforderung: " + \
			str(arglist) + \
			' ' + \
			str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)

