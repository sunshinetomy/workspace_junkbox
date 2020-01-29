import os
import re
import svn.local


try:
	#os.system('start excel.exe "%s"' % "Test")
	raise NameError('HiThere')
	#raise ValueError('HiThere')
	#x = int(input("Please enter a number: "))
#except ValueError:
except Exception as ex:
	dir( Exception )
	dir( ex )
	input("Press enter to exit")
	print( ex )


'''
### Open
while True:
	try:
		#os.system('start excel.exe "%s"' % fullPath)
		#raise NameError('HiThere')
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		input("Press enter to exit")
		print( ValueError )
		break




while True:
	try:
		x = int(input("Please enter a number: "))
		break
	except ValueError:
		print("Oops!  That was no valid number.  Try again...")
		break
		
		
input("Press enter to exit")
'''