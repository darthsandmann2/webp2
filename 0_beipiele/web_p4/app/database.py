import json
import os

class Database( object ):

	def __init__( self, path, file_extension ):
		self._path = path
		self._file_extension = file_extension

	def write( self, filename, data ):
		with open( self._path + str(filename) + self._file_extension, 'w' ) as outfile:
			json.dump( data, outfile )
	
	def read( self, filename ):
		json_data = open( self._path + str(filename) + self._file_extension, 'r' )
		data = json.load( json_data )
		json_data.close()
		return data
	
	def erase( self, filename ):
		os.remove( self._path + str(filename) + self._file_extension )

	def exists( self, filename ):
		return os.path.exists( self._path + str(filename) + self._file_extension )
