import sys
import shutil
import svn.local
from inputAndConfirm import inputAndConfirm

### CONST
TYPE_RAW = 'modified'
LOCAL_PATH = "D:\\workspace_junkbox_temp\\Test_Repository_Trunk"
TEST_SRC = 'D:\\workspace_junkbox_temp\\test_01.txt'
TEST_DST = 'D:\\workspace_junkbox_temp\\Test_Repository_Trunk\\test_01.txt'

#DATA_SRC = "C:\\workspace_L\\ProjectL_Client_3.4.0"
#DATA_DST = "C:\\workspace_L\\ProjectL_Client_3.4.0\\Assets\\AssetBundles\\Localization"


### Message Input
message = inputAndConfirm()

if 'auto' == message:
	message = "[정경진]\n - 번역 데이터 갱신"

	
### Repository Update	
#srcR = svn.local.LocalClient( LOCAL_PATH )
dstR = svn.local.LocalClient( TEST_DST )
dstR.update()
	
### Data Copy
shutil.copyfile( TEST_SRC, TEST_DST )


### Data Commit
fileList = []
for e in dstR.status():
	if TYPE_RAW == e.type_raw_name or TYPE_RAW == "":
		fileList.append( e.name )
	else:
		continue
		
dstR.commit( message, fileList )

		
input("Press enter to exit")
	

	

	
