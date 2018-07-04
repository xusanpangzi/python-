import xlrd
import pymysql
db=pymysql.connect("localhost","root","32386964","python",charset="utf8")
cursor=db.cursor()
cursor.execute("drop table if exists 城市信息")
sql="""create table 城市信息(
       id char (6) not null,
       city char (8) not null); 
"""
cursor.execute(sql)
city=xlrd.open_workbook('city.xls')
text=city.sheet_by_name('text')
row_num=text.nrows
print(row_num)
for i in range(row_num):
    date=text.row_values(i)
    print(date)
    insert="insert into 城市信息 (id,city)values('%c','%s')"%(date[0],date[1])
    cursor.execute(insert)
    db.commit()
db.close()