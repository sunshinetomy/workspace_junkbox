import os
import sys

bundleName = sys.argv[1]

androidSdkPath = 'C:\\Users\\NHNEnt\\AppData\\Local\\Android\\Sdk\\platform-tools\\'
command = 'adb forward tcp:54999 localabstract:Unity-{' + bundleName + '}'

print( androidSdkPath + command )
os.system( androidSdkPath + command )
