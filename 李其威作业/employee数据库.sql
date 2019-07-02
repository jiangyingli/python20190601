CREATE TABLE employee (
	id INT       PRIMARY KEY,
	NAME VARCHAR(20),
	sex VARCHAR(2),
	age INT,
	address VARCHAR(10)
)
INSERT INTO employee (id,NAME,sex,age,address)
VALUES ('1','张三','女','19','北京')
VALUES ('2','李四','男','20','上海')
VALUES ('3','王五','女','25','广州')
VALUES ('4','薛六','女','20','北京')
VALUES ('5','王五','男','22','北京')
VALUES ('6','赵七','男','28','上海')
VALUES ('7','张四','女','23','北京')

#为什么建不成表呢



# （1）. 写出sql语句，查询所有年龄大于20岁的员工（2分）
SELECT * FROM employee WHERE age>20
# （2）. 写出sql语句，查询所有年龄小于25岁的女性员工（3分）
SELECT * FROM employee WHERE age>20 AND sex='女'
# （3）. 写出sql语句，统计男女员工各有多少名（3分）
SELECT COUNT(*) FROM employee GROUP BY sex='男'
SELECT COUNT(*) FROM employee GROUP BY sex='女'
# （4）. 写出sql语句，按照年龄倒序获取员工信息（3分）
SELECT * FROM employee ORDER BY age DESC
# （5）. 写出sql语句，获取员工中哪个姓名具有重名现象（3分）
SELECT COUNT(*) FROM employee GROUP BY NAME 
# （6）. 写出sql语句，查询所有姓张的员工（3分）
SELECT * FROM employee WHERE NAME LIKE '张%'
# （7）. 写出sql语句，查询住址为北京的前3条记录（3分）
SELECT * FROM employee WHERE address='北京' LIMIT 0,3
# （8）. 写出sql语句，查询员工总数（3分）
SELECT COUNT(*) FROM employee
# （9）. 写出sql语句，向表中插入一条记录（2分）
VALUES ('*','**','*','**','**')
# （10）.写出sql语句，修改员工张四的住址为南京（2分）
UPDATE employee SET NAME ='张四' WHERE address='南京'
# （11）.写出sql语句，删除年龄大于24岁的女员工（2分）
DELETE FROM student WHERE number >24 AND sex='女'
