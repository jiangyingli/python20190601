CREATE TABLE employee (
id INT              PRIMARY KEY,
NAME VARCHAR(20),
Sex VARCHAR(2),
Age INT,
Address VARCHAR(500)
)


INSERT INTO employee VALUES (1,'张三','女',19,'北京');
INSERT INTO employee VALUES (2,'李四','男',20,'上海');
INSERT INTO employee VALUES (3,'王五','女',25,'广州');
INSERT INTO employee VALUES (4,'薛六','女',20,'北京');
INSERT INTO employee VALUES (5,'王五','男',22,'北京');
INSERT INTO employee VALUES (6,'赵七','男',28,'上海');
INSERT INTO employee VALUES (7,'张四','女',23,'北京');

# （1）. 写出sql语句，查询所有年龄大于20岁的员工
SELECT * FROM employee WHERE Age > 20
# （2）. 写出sql语句，查询所有年龄小于25岁的女性员工
SELECT * FROM employee WHERE Age < 25 AND Sex = '女'
# （3）. 写出sql语句，统计男女员工各有多少名
SELECT COUNT(*) FROM employee WHERE Sex='女'
SELECT COUNT(*) FROM employee WHERE Sex='男'
# （4）. 写出sql语句，按照年龄倒序获取员工信息
SELECT * FROM employee ORDER BY Age DESC
# （5）. 写出sql语句，获取员工中哪个姓名具有重名现象
SELECT NAME ,COUNT(*)FROM employee GROUP BY NAME
# （6）. 写出sql语句，查询所有姓张的员工
SELECT * FROM employee WHERE NAME LIKE '张%'
# （7）. 写出sql语句，查询住址为北京的前3条记录
SELECT * FROM employee WHERE Address='北京'LIMIT 0,3
# （8）. 写出sql语句，查询员工总数
SELECT COUNT(*) FROM employee
# （9）. 写出sql语句，向表中插入一条记录
INSERT INTO employee VALUES (id,'NAME','Sex',Age,'Address');
# （10）.写出sql语句，修改员工张四的住址为南京
DELETE FROM employee WHERE NAME='张四'
INSERT INTO employee VALUES (7,'张四','女',23,'南京');
# （11）.写出sql语句，删除年龄大于24岁的女员工
DELETE FROM employee WHERE Age>24 AND Sex ='女'