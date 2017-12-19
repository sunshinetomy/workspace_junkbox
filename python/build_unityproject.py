import os

print( 'Start TheMusician_u autobuild' )

#origin = '"C:\Program Files\Unity_563f1\Editor\Unity.exe" -quit -batchmode -projectPath E:\workspace_Musician\musician_u\Musician_Unity -executeMethod BuildScript.BuildAndroid'
#command = '\"C:\\Program Files\\Unity_563f1\\Editor\\Unity.exe\" -quit -batchmode -projectPath E:\workspace_Musician\musician_u\Musician_Unity -executeMethod BuildScript.BuildAndroid'

unityPath = '\"C:\\Program Files\\Unity_563f1\\Editor\\Unity.exe\"'
projectPath = 'E:\workspace_Musician\musician_u\Musician_Unity'
arguments = '-quit -batchmode -projectPath'
executeMethod = '-executeMethod BuildScript.BuildAndroid'

command = unityPath + ' ' + arguments + ' ' + projectPath + ' ' + executeMethod
print ( command )

os.system( command )

print( 'End TheMusician_u autobuild' )