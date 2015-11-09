
class Counter( object ):

	#counter_file =  open('./ID_File.txt', 'r+')

	def read( self ):
		counter_file =  open('./ID_File.txt', 'r')
		counter = counter_file.read()
		counter = int( counter )
		counter_file.close()
		return counter

	def increase( self, n ):
		counter_file =  open('./ID_File.txt', 'r')
		counter = counter_file.read()
		counter = int( counter )
		counter_file.close()
		counter += n
		counter_file = open( './ID_File.txt', 'w')
		counter_file.write( str( counter ) )
		counter_file.close()

	def decrease( self, n ):
		counter_file =  open('./ID_File.txt', 'w')
		counter = counter_file.read()
		counter = int( counter )
		counter -= n
		counter_file.write( str( counter ) )
		counter_file.close()