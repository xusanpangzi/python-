import xlrd
import pymysql
db=pymysql.connect("local","root","32386964","python",charst="utf8")
cursor=db.cursor()
cursor.execute("drop table if exists 数字信息")
sql="""create table 数字信息(
        one )"""