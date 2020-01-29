'''
d:\temp>echo %PATHEXT%
.COM;.EXE;.BAT;.CMD;.VBS..... ;.PYW;.PY

d:\temp>assoc | findstr ".py"
.py=Python.File
.pyc=Python.CompiledFile
.pyo=Python.CompiledFile
.pys=pysFile
.pyw=Python.NoConFile

d:\temp>assoc .py=Python.File
.py=Python.File

d:\temp>ftype | findstr "python"
Python.CompiledFile="C:\Python36\python.exe" "%1" %*
Python.File="C:\Python36\python.exe" "%1" %*
Python.NoConFile="C:\Python36\python.exe" "%1" %*

d:\temp>ftype Python.File="C:\Python36\python.exe" "%1" %*
Python.File="C:\Python34\python.exe" "%1" %*

PATH 에도 실행 스크립트 경로 추가 필요!!

액세스가 거부되었습니다. ( Wind+CMD => Shift + Ctrl + Enter )

from https://soooprmx.com/archives/6471
'''

import sys
import os

path = os.environ["PATH"]
list = path.split( ';' )

for v in list:
	print( v )
