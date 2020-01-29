import sys
import shutil
import svn.local
from inputAndConfirm import inputAndConfirm
import os
import subprocess


############ Values
COMMIT_TYPES = ['modified']

#SRC_PATH = 'D:\\workspace_junkbox_temp'
#DST_PATH = 'D:\\workspace_junkbox_temp\\Test_Repository_Trunk'
#FILE_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']

SRC_PATH = "D:\\workspace_L\\004 공용 데이터\\1.번역"
DST_PATH = "C:\\workspace_L\\ProjectL_Client_3.5.0\\Assets\\AssetBundles\\Localization"
FILE_LIST = ['Chinese.txt', 'English.txt', 'Japanese.txt', 'Korean.txt', 'Thai.txt']



############ Message Input
message = inputAndConfirm()

print( "SRC_PATH - " + SRC_PATH )
print( "DST_PATH - " + DST_PATH )

if 'auto' == message:
	message = "[정경진]\n - 번역 데이터 갱신"


	
###### Repository Update	
srcR = svn.local.LocalClient( SRC_PATH )
srcR.update()
dstR = svn.local.LocalClient( DST_PATH )
dstR.update()


	
###### Data Copy
for val in FILE_LIST:
	src = SRC_PATH + '\\' + val
	dst = DST_PATH + '\\' + val
	shutil.copyfile( src, dst )

	

### Data Commit
commitList = []
for e in dstR.status():
	if COMMIT_TYPES.__contains__( e.type_raw_name ):
		commitList.append( e.name )
	else:
		continue

print( 'commit list' )
for v in commitList:
	print( v )
		
#dstR.commit( message, commitList )

input("Press enter to exit")
	
subprocess.Popen(r'explorer '+ DST_PATH)

########################### TEST_CODE
#SRC_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']
#DST_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']
#for idx, val in enumerate( SRC_LIST ):
	#src = SRC_PATH + '\\' + SRC_LIST[idx]
	#dst = DST_PATH + '\\' + DST_LIST[idx]
	#shutil.copyfile( src, dst )
	
