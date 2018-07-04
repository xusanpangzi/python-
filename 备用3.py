from xml.dom import minidom

doc=minidom.Document()
root=doc.createElement('root')
doc.appendChild(root)
student=doc.createElement('student')
student.appendChild(doc.createComment("学生信息表 'id':[名字,数学,语文,英文]"))
student.appendChild(doc.createTextNode(excel))
root.appendChild(student)
with open('try.xml', 'w') as f:
    doc.writexml(f, encoding='utf-8')
    f.close()
