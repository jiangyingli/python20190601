CREATE TABLE employee(
	id INT PRIMARY KEY,
	NAME VARCHAR(20),
	sex VARCHAR(2),
	age INT ,
	address VARCHAR(10)
)

INSERT INTO employee VALUES(1,'张三','女',19,'北京');
INSERT INTO employee VALUES(2,'李四','男',20,'上海');
INSERT INTO employee VALUES(3,'王五','女',25,'广州');
INSERT INTO employee VALUES(4,'薛六','女',20,'北京');
INSERT INTO employee VALUES(5,'王五','男',22,'北京');
INSERT INTO employee VALUES(6,'赵七','男',28,'上海');
INSERT INTO employee VALUES(7,'张四','女',23,'北京');

#1
SELECT*FROM employee WHERE age>20
#2
SELECT*FROM employee WHERE age<20 AND sex='女'
#3
SELECT sex,COUNT(*) FROM employee GROUP BY sex
#4
SELECT*FROM employee ORDER BY age DESC
#5
SELECT NAME,COUNT(*) FROM employee GROUP BY NAME
#6
SELECT*FROM employee WHERE NAME LIKE '张%'
#7
SELECT*FROM employee WHERE address = '北京' LIMIT 0,3
#8
SELECT COUNT(*)FROM employee;
#9
INSERT INTO employee VALUES(8,'赵四','男',18,'长春')
#10
UPDATE employee SET address='南京' WHERE id=7
#11
DELETE FROM employee WHERE age>24










