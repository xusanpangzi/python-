
import xlrd
from xml.dom import minidom

doc = minidom.Document()
root=doc.createElement('root')
doc.appendChild(root)
student=doc.createElement('student')
root.appendChild(student)
student.appendChild(doc.createComment("学生信息表 \n 'id':[名字,数学,语文,英文]"))

excel=xlrd.open_workbook('student.xls')
sheet=excel.sheet_by_name('text')
nrows=sheet.nrows
for row in range(nrows):
    excel=sheet.row_values(row)
    student_information=doc.createTextNode(str(excel)+'\n')
    student.appendChild(student_information)
    root.appendChild(student)

with open('student.xml', 'wb') as f:
    f.write(doc.toprettyxml(indent='\t',newl='\n',encoding='utf-8'))