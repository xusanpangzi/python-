    # 激活码格式为 前两位为字母，后四位为数字
import random
i = 1
list=[]
while i < 200:
    first = random.randint(65, 122)
    if  first<91 :
        F = chr(first)
    elif first>96:
        F=chr(first)
    else:
        F = chr(first + 7)

    two = random.randint(65, 122)
    if two <91:
        T = chr(two)
    elif two>96:
        T=chr(two)
    else:
        T = chr(two + 7)
    n = [random.randint(0, 9) for i in range(4)]
    N = ("".join(str(i) for i in n))
    M = F + T + N

    i += 1
    list.append(M)
for each in list:

    print(each)


