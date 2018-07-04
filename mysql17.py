import xlrd
import pymysql
db=pymysql.connect("localhost","root","32386964","python",charset="utf8")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS 学生信息表")
sql="""CREATE TABLE  学生信息表(
       id char (8) not null,
       名字 char(8) not null,
       数学 int(6) not null,
       语文 int(6) not null,
       英语 int(6) not null);"""
cursor.execute(sql)
student=xlrd.open_workbook('student.xls')
text = student.sheet_by_name("text")
row_num=text.nrows
#print(row_num)
for i in range(0,row_num):
    date=text.row_values(i)
    print(date)
    insert="insert into 学生信息表(id,名字,数学,语文,英语) values ('%c','%s','%d','%d','%d')"% (date[0],date[1],date[2],date[3],date[4])
    cursor.execute(insert)
    db.commit()
db.close()