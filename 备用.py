from xml.dom.minidom import Document
doc = Document()  #创建DOM文档对象
root = doc.createElement('root')
doc.appendChild(root)
item = doc.createElement('item')
DOCUMENT.appendChild(item)
key = doc.createElement('key')

key_text = doc.createTextNode('Key1') #元素内容写入
key.appendChild(key_text)
item.appendChild(key)
'''
display = doc.createElement('display')
item.appendChild(display)
display_url = doc.createElement('url')
display_title  = doc.createElement('title')
display_url_text = doc.createTextNode('https://baidu.com/')
display_title_text  = doc.createTextNode('北京市公积金咨询电话')
display.appendChild(display_url)
display.appendChild(display_title)
display_url.appendChild(display_url_text)
display_title.appendChild(display_title_text)
item.appendChild(display)

price = doc.createElement('price')
price_text = doc.createTextNode('28')
price.appendChild(price_text)
item.appendChild(price)
'''
########### 将DOM对象doc写入文件
f = open('tel.xml','w')
#f.write(doc.toprettyxml(indent = '\t', newl = '\n', encoding = 'utf-8'))
doc.writexml(f,indent = '\t',newl = '\n', addindent = '\t',encoding='utf-8')
f.close()






