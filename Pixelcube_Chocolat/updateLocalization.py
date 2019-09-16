import sys
import shutil
import svn.local
from inputAndConfirm import inputAndConfirm

###### CONST
COMMIT_TYPES = ['modified']
SRC_PATH = 'D:\\workspace_junkbox_temp'
DST_PATH = 'D:\\workspace_junkbox_temp\\Test_Repository_Trunk'

#SRC_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']
#DST_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']
FILE_LIST = ['test_01.txt', 'test_02.txt', 'test_03.txt']

#SRC_PATH = "C:\\workspace_L\\ProjectL_Client_3.4.0"
#SRC_PATH = "C:\\workspace_L\\ProjectL_Client_3.4.0"
#DST_PATH = "C:\\workspace_L\\ProjectL_Client_3.4.0\\Assets\\AssetBundles\\Localization"
#DST_FILES = { "Chinese.txt", "English.txt", 


###### Message Input
message = inputAndConfirm()

if 'auto' == message:
	message = "[정경진]\n - 번역 데이터 갱신"

	
###### Repository Update	
#srcR = svn.local.LocalClient( DST_PATH )
#srcR.update()
dstR = svn.local.LocalClient( DST_PATH )
dstR.update()
	
###### Data Copy
#for idx, val in enumerate( FILE_LIST ):
	#src = SRC_PATH + '\\' + FILE_LIST[idx]
	#dst = DST_PATH + '\\' + FILE_LIST[idx]
	#shutil.copyfile( src, dst )
	
for val in FILE_LIST:
	src = SRC_PATH + '\\' + val
	dst = DST_PATH + '\\' + val
	shutil.copyfile( src, dst )
	print( src )
	print( dst )



### Data Commit
fileList = []
for e in dstR.status():
	print( e.name )
	print( e.type_raw_name )
	
	if COMMIT_TYPES.__contains__( e.type_raw_name ):
		fileList.append( e.name )
	else:
		continue
		
#dstR.commit( message, fileList )

for v in fileList:
	print( fileList )

		
input("Press enter to exit")
	

	

	
