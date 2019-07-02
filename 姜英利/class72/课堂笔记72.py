# 1，MySQL数据库简介，免费的，收费的（oracle，微软，IBM）
# 2，安装，分安装版和绿色版，我们使用绿色版
# 3，数据库与数据库实例介绍
# 4，基本概念：数据库实例，表，字段，类型，长度，
# 5，插入操作，基本查询，修改操作，删除炒作
# 6，高级查询操作，关联嵌套查询，排序，分组

# 素材1
# -- drop database animals;
# -- 1. 使用SQL语句创建数据库 ly19
# -- create database ly19;
# -- 1.1 使用SQL语句创建表 animals
# -- create table animals (id int ,name varchar(10),kind varchar(8),number int ,address varchar(32));
# -- 1.2 向表animals中添加数据
# -- INSERT INTO animals VALUES(1801,'美洲豹','猫科',16663,'墨西哥');
# -- INSERT INTO animals VALUES(1802,'非洲象','象科',357281,'津巴布韦');
# -- INSERT INTO animals VALUES(1803,'亚洲象','象科',52359,'印度');
# -- INSERT INTO animals VALUES(1804,'金钱豹','猫科',78,'孟加拉');
# -- INSERT INTO animals VALUES(1805,'白熊','熊科',21006,'北极');
# -- INSERT INTO animals VALUES(1806,'美洲狮','猫科',130508,'墨西哥');
# -- INSERT INTO animals VALUES(1807,'棕熊','熊科',90086,'阿富汗');
# -- INSERT INTO animals VALUES(1808,'华南虎','猫科',0,'中国');
# -- INSERT INTO animals VALUES(1809,'熊猫','熊科',1668,'中国');
# -- INSERT INTO animals VALUES(1810,'孟加拉虎','猫科',5102,'孟加拉');
# -- INSERT INTO animals VALUES(1811,'东北虎','猫科',21,'中国');
# -- 2. 使用SQL语句查询所有猫科动物信息。
# -- select id as 序号,name as 名称,kind as 种类,number as 数量, address as 产地 from animals where kind='猫科'
# -- 3. 使用SQL语句查询所有数量小于2000的动物信息。
# -- select * from animals where number < 2000;
# -- 4. 使用SQL语句修改“美洲狮”的产地为美国
# -- update animals set address='美国' where name='美洲狮';
# -- 5. 使用SQL语句删除数量大于100000的物种
# -- delete from animals where number>100000


# 素材2
# 1. 已知：员工信息表，表名为：employee
# id	Name	Sex	Age	Address
# 1	    张三	女	19	北京
# 2	    李四	男	20	上海
# 3	    王五	女	25	广州
# 4	    薛六	女	20	北京
# 5	    王五	男	22	北京
# 6	    赵七	男	28	上海
# 7	    张四	女	23	北京
# （1）. 写出sql语句，查询所有年龄大于20岁的员工（2分）
# （2）. 写出sql语句，查询所有年龄小于25岁的女性员工（3分）
# （3）. 写出sql语句，统计男女员工各有多少名（3分）
# （4）. 写出sql语句，按照年龄倒序获取员工信息（3分）
# （5）. 写出sql语句，获取员工中哪个姓名具有重名现象（3分）
# （6）. 写出sql语句，查询所有姓张的员工（3分）
# （7）. 写出sql语句，查询住址为北京的前3条记录（3分）
# （8）. 写出sql语句，查询员工总数（3分）
# （9）. 写出sql语句，向表中插入一条记录（2分）
# （10）.写出sql语句，修改员工张四的住址为南京（2分）
# （11）.写出sql语句，删除年龄大于24岁的女员工（2分）


# 素材3
# CREATE TABLE book (b_code VARCHAR(10),b_name VARCHAR(100),b_author VARCHAR(50),b_publish VARCHAR(100),b_pubdate DATE,b_price DOUBLE(8,2));
# CREATE TABLE reader (r_code VARCHAR(10),r_name VARCHAR(100),r_sex CHAR(1),r_dep VARCHAR(100));
# CREATE TABLE check_out(b_code VARCHAR(10),r_code VARCHAR(10),borrow_date DATE,return_date DATE);
#
# -- 插入图书信息
# INSERT INTO book VALUES('b_001','《幻城》','郭敬明','人民教育出版社','2004-5-21',19.8);
# INSERT INTO book VALUES('b_002','《三重门》','韩寒','电子工业出版社','2001-7-22',22.5);
# INSERT INTO book VALUES('b_003','《幻城》','郭敬明','中国人民大学出版社','2004-5-21',20);
# INSERT INTO book VALUES('b_004','《围城》','钱钟书','人民教育出版社','2010-5-15',21);
# INSERT INTO book VALUES('b_005','《幻城》','郭敬明','清华大学出版社','2011-5-21',22);
# INSERT INTO book VALUES('b_006','《水浒传》','施耐庵','电子工业出版社','2008-3-21',48);
# INSERT INTO book VALUES('b_007','《福尔摩斯》','柯南道尔','人民教育出版社','2004-5-21',33);
# INSERT INTO book VALUES('b_008','《伟大的博弈》','张化龙','电子工业出版社','2009-2-13',28);
# INSERT INTO book VALUES('b_009','《活法》','稻盛和夫','人民教育出版社','2000-1-2',15);
# INSERT INTO book VALUES('b_010','《人性的弱点》','戴尔卡耐基','人民教育出版社','2007-7-31',19.8);
#
# -- 插入读者数据
# INSERT INTO reader VALUES('r_001','丁涛','男','人事部');
# INSERT INTO reader VALUES('r_002','王壮','男','人事部');
# INSERT INTO reader VALUES('r_003','王影影','女','财务部');
# INSERT INTO reader VALUES('r_004','吴俊铖','男','培训部');
# INSERT INTO reader VALUES('r_005','张佳','女','财务部');
# INSERT INTO reader VALUES('r_006','刁钱龙','男','计算机系');
# INSERT INTO reader VALUES('r_007','李佳成','男','财务部');
#
# -- 插入借阅记录信息
# INSERT INTO check_out VALUES('b_003','r_001','2008-4-9','2008-4-22');
# INSERT INTO check_out VALUES('b_003','r_006','2009-4-21','2009-5-10');
# INSERT INTO check_out VALUES('b_004','r_005','2009-10-2','2009-11-1');
# INSERT INTO check_out VALUES('b_001','r_003','2010-3-12','2010-4-1');
# INSERT INTO check_out VALUES('b_009','r_002','2010-3-22','2010-4-5');
# INSERT INTO check_out VALUES('b_008','r_001','2010-8-11','2010-9-3');
# INSERT INTO check_out VALUES('b_009','r_007','2010-12-3','2010-12-31');
# INSERT INTO check_out VALUES('b_003','r_004','2011-4-8','2011-5-7');
# INSERT INTO check_out VALUES('b_001','r_003','2012-4-9',NULL);


# 1、查询在2008年的所有借书信息；
# 2、查询丁涛一共借过几本书；
# 3、查询人事部的借书信息；
# 4、查询被借次数最多的图书的名称；
# 5、查询未归还的图书；
# 6、查询人民教育出版社的图书数量；
# 7、查询价格最贵的图书；
# 8、查询价格最便宜的书被谁借阅过；


