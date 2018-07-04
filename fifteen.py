import xlwt
import json
from collections import OrderedDict
txt=open('city.txt','r').read()
#print(txt)
city=xlwt.Workbook()
text=city.add_sheet("text")
information=json.loads(txt,object_pairs_hook=OrderedDict)
#print(information)
for row,i in enumerate(list(information)):
        text.write(row,0,i)
        #print(information[i])
        text.write(row,1,information[i])
city.save("city.xls")