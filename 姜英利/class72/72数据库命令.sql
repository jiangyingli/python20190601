#创建数据库
CREATE DATABASE python01;

#删除数据库
DROP DATABASE python01 ;

#创建表
CREATE TABLE student (
	number VARCHAR(10) PRIMARY KEY,
	NAME VARCHAR(20),
	sex VARCHAR(2),
	birthday DATE,
	address VARCHAR(500),
	height INT
);

DROP TABLE student;

INSERT INTO student(number,NAME,sex,birthday,address,height)
VALUES ('1001','张三','男','2010-01-01','吉林长春','179')

#正确性，学号不允许重复
#PRIMARY KEY：主键，主关键字

#更新表数据
UPDATE student SET NAME='张四' WHERE number='1001';

#删除数据
DELETE FROM student WHERE number='1001';

#查询数据
SELECT * FROM student WHERE number='1001';


CREATE TABLE animals (
	id INT PRIMARY KEY,
	NAME VARCHAR(10),
	kind VARCHAR(8),
	number INT ,
	address VARCHAR(32)
);

INSERT INTO animals VALUES(1801,'美洲豹','猫科',16663,'墨西哥');
INSERT INTO animals VALUES(1802,'非洲象','象科',357281,'津巴布韦');
INSERT INTO animals VALUES(1803,'亚洲象','象科',52359,'印度');
INSERT INTO animals VALUES(1804,'金钱豹','猫科',78,'孟加拉');
INSERT INTO animals VALUES(1805,'白熊','熊科',21006,'北极');
INSERT INTO animals VALUES(1806,'美洲狮','猫科',130508,'墨西哥');
INSERT INTO animals VALUES(1807,'棕熊','熊科',90086,'阿富汗');
INSERT INTO animals VALUES(1808,'华南虎','猫科',0,'中国');
INSERT INTO animals VALUES(1809,'熊猫','熊科',1668,'中国');
INSERT INTO animals VALUES(1810,'孟加拉虎','猫科',5102,'孟加拉');
INSERT INTO animals VALUES(1811,'东北虎','猫科',21,'中国');



#复杂的查询
SELECT * FROM animals ORDER BY number;


SELECT * FROM animals ORDER BY number DESC ;


#group by 分组查询
#以谁分组，谁能显示
SELECT kind,COUNT(*) FROM animals GROUP BY kind ;

#指定列
SELECT * FROM animals;
SELECT NAME,number FROM animals;

#多条件
SELECT * FROM animals WHERE kind='猫科' AND number>10000;
SELECT * FROM animals WHERE kind='猫科' OR number>10000;

#查询一部分
SELECT * FROM animals LIMIT 3,3;

#常用函数
SELECT MIN(number) FROM animals;
SELECT MAX(number) FROM animals;
SELECT AVG(number) FROM animals;

#模糊查询,%匹配任意多字符（0-∞），_ 匹配一个字符
SELECT * FROM animals WHERE NAME LIKE '美%';
SELECT * FROM animals WHERE NAME LIKE '美_';

