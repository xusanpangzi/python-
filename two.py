import pymysql
import random
db = pymysql.connect("localhost", "root", "32386964", "python")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS jihuoma")
sql = """CREATE TABLE jihuoma (
         t int(3) not null primary key,
         number char(10) not null 
         );"""
cursor.execute(sql)
i = 1
list=[]
while i < 201:
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

f=1
for each in list:
    j = "INSERT INTO jihuoma(t, number) VALUES ('%d','%s')" % (f, each)
    cursor.execute(j)
    db.commit()
    f += 1
db.close()


