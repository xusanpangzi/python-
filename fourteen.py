import xlwt
import json
from collections import OrderedDict
txt=open('student.txt','r').read()
#print(txt)
student=xlwt.Workbook()
text=student.add_sheet("text",cell_overwrite_ok = True)
t = json.loads(txt,object_pairs_hook=OrderedDict)
#print(list(t))
for row, i in enumerate(list(t)):
        print(row,i)
        text.write(row, 0, i)
        for col, j in enumerate(t[i]):
            text.write(row, col+1, j)
            #print(row,col+1,j)
student.save('student.xls')