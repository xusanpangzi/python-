from bs4 import BeautifulSoup
html=open('eight.html','r',encoding='UTF-8').read()
soup=BeautifulSoup(html,'html.parser')
links=soup.find_all('link')
#观察发现，这个文件里链接标记都是 link
for link in links:
    print(link)