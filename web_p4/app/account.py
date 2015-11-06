import json
from app import converter
from app import counter
from app import database
from app import validator

class Account( object ):

	def __init__( self ):
		self._path = "./data/"
		self._file_extension = ".json"
		self._counter = counter.Counter()
		self._converter = converter.Converter()
		self._database = database.Database( self._path, self._file_extension )
		self._validator = validator.Validator( self._database, self._counter )

	def registration( self, **form_data ):
		new_ident = str( self._counter.read() )
		self._counter.increase( 1 )
		form_data.update( {'ID':new_ident} )
		json_data = self._converter.jsonify( **form_data )
		self._database.write( new_ident, form_data )

	def edit( self, **form_data ):
		if( self._validator.validate( "vorname", "nachname", "passwort", **form_data ) ):
			if( form_data.get( 'loeschen' ) == "yes" ):
				self._database.erase( form_data.get( 'ID' ) )
			else:
				self._database.write( form_data.get( 'ID' ), form_data )
			return 1
		else:
			return 0
		
