import os
import re
import sys
import svn.local

#reload( sys )


REGULAR = "라인팝쇼콜라_개발일정_.*"
FILE = ""
PATH = "D:\\workspace_L\\002 서비스 플랜"



### FileName
regul = re.compile( REGULAR )
file_list = os.listdir( PATH )

for file in file_list:
	matched = regul.match( file )
	if matched:
		FILE = matched.string

print( FILE )

### 성공할 떄까지 반복
### 엑셀파일이 utf-8이 아니기 때문에 파일 열기 작업에서 decode 에러가 발생할 수 있다??
result = -1
while result != 0:
	try:
	### Update
		r = svn.local.LocalClient( PATH )
		r.update()
		
		fullPath = PATH + "\\" + FILE

	### Open
		result = os.system('start excel.exe "%s"' % fullPath)
		
		exit()
	except Exception as ex:
		print( "Exception = " + ex )
		input("Press enter to exit")
