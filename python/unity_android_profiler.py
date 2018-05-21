import os
import sys

#ADB@127.0.0.1:54999
#adb kill-server
#adb start-server
#방화벽 설정 > 고급 설정 > Outbound Rules > 새규칙 > 포트 54998-55511 > 생성

bundleName = sys.argv[1]

androidSdkPath = 'C:\\Users\\NHNEnt\\AppData\\Local\\Android\\Sdk\\platform-tools\\'
command = 'adb forward tcp:54999 localabstract:Unity-{' + bundleName + '}'

print( androidSdkPath + command )
os.system( androidSdkPath + command )
