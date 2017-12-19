import os

notepadPPPath = '\"C:\\Program Files (x86)\\Notepad++\\notepad++.exe\"'
unityLogPath = 'C:\\Users\\rhymus_client_118\\AppData\\Local\\Unity\\Editor\\Editor.log'

print( notepadPPPath + ' ' + unityLogPath )
os.system( notepadPPPath + ' ' + unityLogPath )
