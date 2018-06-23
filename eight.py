#碰到关于html格式的东西，尽可能用html编译器，beautifulsoup库
from bs4 import BeautifulSoup
html=open('eight.html','r',encoding='UTF-8').read()
soup=BeautifulSoup(html, "html.parser")
txt=soup.find_all('article')
print(txt)