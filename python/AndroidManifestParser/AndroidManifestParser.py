import os

command = 'java -jar AXMLPrinter2.jar AndroidManifest.xml > print.txt'

print( command )
os.system( command )
