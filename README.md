# python-example
编程习题 记录
#zero
制作微信未读头像。没有接触过python图像有关的东西，查询之后运用PIL生成，其中用到的类有 ImageDraw,ImageFont,Image.
用到的方法有ImageDraw.Draw()   Image.open()    imageFont.truetype()    __.text()    __.save()
#one
生成激活码，我本来不知道有uuid这个库，可以产生32位的激活码，12-4-4-12.所以我自己定义了一个生成激活码的模板，前两位为字母，后四位数字（非常弱智）。
后来了解到uuid，很好用。
#two
将生成的激活码存入mysql。学习了MySQL，只掌握了几个基本语句，在mysql客户端操作时要注意执行命令用分号！！！
show database；（展示所有数据库）  create database A;（创建名为A的数据库） use A；（进入使用A数据库）   
create table B  （在A中创建名为B的数据表）
->（
->id char(10) not null primary key, (创建一列名为id，数据类型为char，字符串最大值为10，不为空，主键)
->name char(16) not null ,  (创建名为name一列)
->sex char(6) not null,
->age int not null,
);
insert into  B set values(" "," "," ");  (B表中添加数据)
select * from B;  (展示B表所有列信息)   select id from B； （展示B表的id列）
update B set id =" C "where name=' D '；(将姓名为D的id改为C) update B set age=age+1; (将所有人年龄加1)
delete from B；（删除B表中所有数据）   delete from B where name=‘ D’；（将姓名为D 的一行删除）
alter table B change name NAME char(16) not null; (将name修改为NAME)
alter table B change sex sex char(10) not null ;(将sex的字符最大值改为10)
alter table B drop 列名；（删除这列）  alter table B rename BB；（重命名表名为BB）
drop table B；（删除B表）  drop batadase A；（删除A数据库）
进阶：
修改Mysql数据库的登陆密码  mysqladmin -r root -p password 新密码
文件方式创建数据表 （文件里的内容格式就是上面创建表的格式） mysql -D 库名 -h 主机名 -u root -p <.sql  （sql类型文件）
接下来就是题目里用到的 MySQL与python建立联系

