import json

class Converter( object ):

	def jsonify( self, **form_input ):
		return json.dumps( form_input, separators=(',',':') )
