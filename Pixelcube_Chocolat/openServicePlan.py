import os
import svn.local

FILE = "라인팝쇼콜라_개발일정_190902.xlsx"
PATH = "D:\\workspace_L\\002 서비스 플랜"

r = svn.local.LocalClient( PATH )
r.update()

fullPath = PATH + "\\" + FILE

os.system('start excel.exe "%s"' % fullPath)
exit()

