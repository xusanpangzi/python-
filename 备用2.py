import pymysql
db=pymysql.connect("localhost","root","32386964","python",charset="utf8")
cursor=db.cursor()
cursor.execute("DROP TABLE IF EXISTS student")
sql="""CREATE TABLE  student(
       id int (2) not null primary key,
       名字 char(8) not null,
       数学 int(6) not null,
       语文 int(6) not null,
       英语 int(6) not null);"""
cursor.execute(sql)







