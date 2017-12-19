import os

androidSdkPath = 'E:\\android_sdk\\platform-tools\\'
command = 'adb root'

print( androidSdkPath + command )
os.system( androidSdkPath + command )
