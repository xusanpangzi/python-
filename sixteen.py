import xlwt
import json
from collections import OrderedDict
txt=open('numbers.txt','r').read()
#print(txt)
numbers=xlwt.Workbook()
sheet=numbers.add_sheet("sheet")
t=json.loads(txt,object_pairs_hook=OrderedDict)
#print(t[1][2])
for row,i in enumerate(t):
    #print(row,i)
    for j in range(3):
        sheet.write(row,j,i[j])

numbers.save('numbers.xls')