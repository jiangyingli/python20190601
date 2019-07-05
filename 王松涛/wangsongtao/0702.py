CREATE DATABASE wangsongtao111;
CREATE TABLE employee(
       id  VARCHAR(7) ,
       NAME  VARCHAR(7),
       sex  VARCHAR(2),
       age  VARCHAR(6),
       address  VARCHAR(500),
)
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('1','张三','女','19','北京')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('2','李四','男','20','上海')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('3','王五','女','25','广州')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('4','薛六','女','20','北京')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('5','王五','男','22','北京')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('6','赵七','男','28','上海')
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('7','张四','女','23','北京')
#1
SELECT*FROM employee WHERE age> 20
#2
SELECT*FROM employee WHERE age< 25 AND sex'女'
#3
SELECT
#4
SELECT * FROM employee ORDER BY age DESC
#5
SELECT * FROM employee WHERE NAME = NAME
#6
SELECT * FROM employee WHERE NAME LIKE '张%'
#7
SELECT * FROM employee WHERE address = '北京'LIMIT 0,3
#8
SELECT * FROM employee
#9
INSERT INTO employee (id,NAME,sex,age,address)
#10
UPDATE employee SET address='南京'WHERE NAME = '张四'
#11
DELETE FROM employee WHERE age>24 sex='女'
