from mako import exceptions
import json
from app import database
from app import view

class Validator( object ):

	def __init__( self, database, counter ):
		self._database = database
		self._counter = counter

	def validate( self, *to_check, **form_input ):
		counter = 0
		fails = ""
		ident = form_input.get( 'ID' )
		data = self._database.read( ident )
		if( not self._database.exists( ident ) ):
			pass # Fehlerbehandlung
			return 0
		for key in to_check:
			if( form_input.get( key ) == data[key] ):
				counter += 1
			else:
				fails += key + ", "
		if( counter == len( to_check ) ):
			return 1
		else:
			return 0
