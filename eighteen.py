from xml.dom import minidom
import xlrd
doc=minidom.Document()
root=doc.createElement("root")
doc.appendChild(root)
cities=doc.createElement("cities")
cities.appendChild(doc.createComment("城市信息"))
root.appendChild(cities)

excel=xlrd.open_workbook('city.xls')
sheet=excel.sheet_by_name("text")
nrows=sheet.nrows
#print(nrows)
for row in range(nrows):
    e=sheet.row_values(row)
    city_information=doc.createTextNode(str(e))
    cities.appendChild(city_information)
    root.appendChild(cities)
with open('city.xml','wb')as f:
    f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))