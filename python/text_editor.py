import os
import json
import shutil


f = open( "build.gradle", 'r+' )
data = f.read()
#f.close()
#print ( data )

data = data.replace( "classpath 'com.android.tools.build:gradle:2.1.0'", "classpath 'com.android.tools.build:gradle:2.3.0'" )
#print ( data )

#f = open( "build.gradle", 'w' )
#print ( data )

f.seek( 0 )
f.write( data )
f.close()
