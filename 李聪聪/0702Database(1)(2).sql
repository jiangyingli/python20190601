#素材1
#1
CREATE TABLE animals (
	id INT PRIMARY KEY,
	NAME VARCHAR(10),
	kind VARCHAR(8),
	number INT ,
	address VARCHAR(32)
)

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
#2使用SQL语句查询所有猫科动物信息
SELECT * FROM animals WHERE kind='猫科';
#3使用SQL语句查询所有数量小于2000的动物信息
SELECT * FROM animals WHERE number<2000;
#4使用SQL语句修改“美洲狮”的产地为美国
UPDATE animals SET address='美国' WHERE NAME='美洲狮';
#5使用SQL语句删除数量大于100000的物种
DELETE FROM animals WHERE number>100000;

#素材2
CREATE TABLE employee (
	id INT PRIMARY KEY,
	NAME VARCHAR(4),
	sex VARCHAR(2),
	age INT ,
	address VARCHAR(4)
)

INSERT INTO employee VALUES(1,'张三','女',19,'北京');
INSERT INTO employee VALUES(2,'李四','男',20,'上海');
INSERT INTO employee VALUES(3,'王五','女',25,'广州');
INSERT INTO employee VALUES(4,'薛六','女',20,'北京');
INSERT INTO employee VALUES(5,'王五','男',22,'北京');
INSERT INTO employee VALUES(6,'赵七','男',28,'上海');
INSERT INTO employee VALUES(7,'张四','女',23,'北京');
#1查询所有年龄大于20岁的员工
SELECT * FROM employee WHERE age>20;
#2查询所有年龄小于25岁的女性员工
SELECT * FROM employee WHERE age<25 AND sex='女';
#3统计男女员工各有多少名
SELECT sex,COUNT(*) FROM employee GROUP BY sex;
#4按照年龄倒序获取员工信息
SELECT * FROM employee ORDER BY age DESC;
#5获取员工中哪个姓名具有重名现象
SELECT NAME ,COUNT(*) FROM employee GROUP BY NAME WHERE COUNT>1;
#6查询所有姓张的员工
SELECT * FROM employee WHERE NAME LIKE '张%';
#7查询住址为北京的前3条记录
SELECT * FROM employee WHERE address='北京' LIMIT 0,3;
#8查询员工总数
SELECT COUNT(*) FROM employee;
#9向表中插入一条记录
#10修改员工张四的住址为南京
UPDATE employee SET address='南京' WHERE NAME='张四';
#11删除年龄大于24岁的女员工
DELETE FROM employee WHERE age>24 AND sex='女';
