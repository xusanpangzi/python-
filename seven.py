import os
import glob
files=glob.glob(r'C:\Users\qqq\PycharmProjects\untitled\*')
code=0
note=0
for file in files:
    os.chdir(file)
    pys=glob.glob('*.py')
    for py in pys:
        lines=open(py,'r',encoding='UTF-8').readlines()
        for line in lines:
            if "#" in line:
                note+=1
            else:
                code+=1

print("我所编代码中共有注释{}行，代码{}行".format(note,code))


