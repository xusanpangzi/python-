import xlrd
from xml.dom import minidom
doc=minidom.Document()
root=doc.createElement("root")
doc.appendChild(root)
numbers=doc.createElement("numbers")
root.appendChild(numbers)
numbers.appendChild(doc.createComment("数字信息"))
excel=xlrd.open_workbook("numbers.xls")
sheet=excel.sheet_by_name("sheet")
nrows=sheet.nrows
print(nrows)
for row in range(nrows):
    e=sheet.row_values(row)
    print(e)
    number_information=doc.createTextNode(str(e))
    numbers.appendChild(number_information)
with open("numbers.xml","wb")as f:
    f.write(doc.toprettyxml(encoding='utf-8'))
