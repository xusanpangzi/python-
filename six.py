import glob
from collections import Counter
dairys=glob.glob(r'C:\Users\qqq\PycharmProjects\untitled\python小项目\dairy\*.txt')
for dairy in dairys:
    txt=open(dairy.replace("\\","/"),"r").read()
    file=txt.split()
    c=Counter(file)
    print(c.most_common(1))
