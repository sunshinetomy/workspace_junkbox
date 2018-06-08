import os
import sys

androidSdkPath = 'C:\\Users\\NHNEnt\\AppData\\Local\\Android\\Sdk\\platform-tools\\'
command_01 = 'adb tcpip 5555'
command_02 = 'adb connect 10.78.103.222'

print( androidSdkPath + command_01 )
os.system( androidSdkPath + command_01 )

# 핸드폰을 분리하고

print( '핸드폰을 분리하고' )

#os.system( androidSdkPath + command_02 )
