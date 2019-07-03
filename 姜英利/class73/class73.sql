

SELECT NAME,COUNT(*) AS 数量 FROM employee GROUP BY NAME
HAVING COUNT(*)>1

HAVING:分组之后条件判断用HAVING

CREATE TABLE book(
	number VARCHAR(20) PRIMARY KEY,#最大字节数
	NAME VARCHAR(500),
	author VARCHAR(100),
	price FLOAT
)
CREATE TABLE author(
	number VARCHAR(20) PRIMARY KEY,
	NAME VARCHAR(20),
	address VARCHAR(20),
	message VARCHAR(20)
)

#属性和表无关

#再创建一个新表
#作者表


关联的表，关联关系，作者的number和图书的author
关联的字段一般要求类型一致


关联查询

SELECT * FROM book,author
WHERE  author.number=book.author


#查看所有人的写书信息
#左外连接,主表信息全显示，根据关联关系，从辅表获取数据
#左外连接，优先左
SELECT * FROM author
LEFT JOIN book ON author.number=book.author

#右外连接，优先右
SELECT * FROM author 
RIGHT JOIN book ON author.number=book.author

#嵌套查询
#一个查询作为另一个查询的条件

#哪本书最贵
SELECT * FROM book WHERE price =(SELECT MAX(price) FROM book)


# 素材3
CREATE TABLE book (b_code VARCHAR(10),b_name VARCHAR(100),b_author VARCHAR(50),b_publish VARCHAR(100),b_pubdate DATE,b_price DOUBLE(8,2));
CREATE TABLE reader (r_code VARCHAR(10),r_name VARCHAR(100),r_sex CHAR(1),r_dep VARCHAR(100));
CREATE TABLE check_out(b_code VARCHAR(10),r_code VARCHAR(10),borrow_date DATE,return_date DATE);
#
-- 插入图书信息
INSERT INTO book VALUES('b_001','《幻城》','郭敬明','人民教育出版社','2004-5-21',19.8);
INSERT INTO book VALUES('b_002','《三重门》','韩寒','电子工业出版社','2001-7-22',22.5);
INSERT INTO book VALUES('b_003','《幻城》','郭敬明','中国人民大学出版社','2004-5-21',20);
INSERT INTO book VALUES('b_004','《围城》','钱钟书','人民教育出版社','2010-5-15',21);
INSERT INTO book VALUES('b_005','《幻城》','郭敬明','清华大学出版社','2011-5-21',22);
INSERT INTO book VALUES('b_006','《水浒传》','施耐庵','电子工业出版社','2008-3-21',48);
INSERT INTO book VALUES('b_007','《福尔摩斯》','柯南道尔','人民教育出版社','2004-5-21',33);
INSERT INTO book VALUES('b_008','《伟大的博弈》','张化龙','电子工业出版社','2009-2-13',28);
INSERT INTO book VALUES('b_009','《活法》','稻盛和夫','人民教育出版社','2000-1-2',15);
INSERT INTO book VALUES('b_010','《人性的弱点》','戴尔卡耐基','人民教育出版社','2007-7-31',19.8);
#
-- 插入读者数据
INSERT INTO reader VALUES('r_001','丁涛','男','人事部');
INSERT INTO reader VALUES('r_002','王壮','男','人事部');
INSERT INTO reader VALUES('r_003','王影影','女','财务部');
INSERT INTO reader VALUES('r_004','吴俊铖','男','培训部');
INSERT INTO reader VALUES('r_005','张佳','女','财务部');
INSERT INTO reader VALUES('r_006','刁钱龙','男','计算机系');
INSERT INTO reader VALUES('r_007','李佳成','男','财务部');
#
-- 插入借阅记录信息
INSERT INTO check_out VALUES('b_003','r_001','2008-4-9','2008-4-22');
INSERT INTO check_out VALUES('b_003','r_006','2009-4-21','2009-5-10');
INSERT INTO check_out VALUES('b_004','r_005','2009-10-2','2009-11-1');
INSERT INTO check_out VALUES('b_001','r_003','2010-3-12','2010-4-1');
INSERT INTO check_out VALUES('b_009','r_002','2010-3-22','2010-4-5');
INSERT INTO check_out VALUES('b_008','r_001','2010-8-11','2010-9-3');
INSERT INTO check_out VALUES('b_009','r_007','2010-12-3','2010-12-31');
INSERT INTO check_out VALUES('b_003','r_004','2011-4-8','2011-5-7');
INSERT INTO check_out VALUES('b_001','r_003','2012-4-9',NULL);


1、查询在2008年的所有借书信息；
SELECT * FROM check_out,book,reader
WHERE check_out.b_code=book.b_code 
AND check_out.r_code=reader.r_code
AND borrow_date LIKE '2008%'



2、查询丁涛一共借过几本书；
SELECT COUNT(*) FROM check_out,reader
WHERE check_out.r_code=reader.r_code
AND reader.r_name='丁涛'


3、查询人事部的借书信息；
SELECT * FROM check_out,book,reader
WHERE check_out.b_code=book.b_code 
AND check_out.r_code=reader.r_code
AND reader.r_dep = '人事部'


4、查询被借次数最多的图书的名称；
SELECT * FROM book WHERE b_code=(
SELECT b_code FROM check_out GROUP BY b_code
ORDER BY COUNT(*) DESC LIMIT 0,1)


5、查询未归还的图书；
SELECT * FROM check_out,book 
WHERE check_out.b_code = book.b_code
AND return_date IS NULL
#null这个值，需要用is来判断，不是null 用is not null

6、查询人民教育出版社的图书数量；
SELECT COUNT(*) FROM book WHERE b_publish = '人民教育出版社'

7、查询价格最贵的图书；


8、查询价格最便宜的书被谁借阅过；

SELECT * FROM reader,check_out 
WHERE check_out.r_code=reader.r_code
AND b_code=(
SELECT b_code FROM book WHERE b_price = (
SELECT MIN(b_price) FROM book )
)

