CREATE TABLE employee (
	id VARCHAR(4) PRIMARY KEY,
	NAME VARCHAR(20),
	sex VARCHAR(2),
	age INT,
	address VARCHAR(10)
	)
INSERT INTO employee VALUES(1,"张三","女",19,"北京");
INSERT INTO employee VALUES(2,"李四","男",20,"上海");
INSERT INTO employee VALUES(3,"王五","女",25,"广州");
INSERT INTO employee VALUES(4,"薛六","女",20,"北京");
INSERT INTO employee VALUES(5,"王五","男",22,"北京");
INSERT INTO employee VALUES(6,"赵七","男",28,"上海");
INSERT INTO employee VALUES(7,"张四","女",23,"北京")

SELECT * FROM employee WHERE age>20;
SELECT*FROM employee WHERE age<25 AND sex='女';
SELECT sex,COUNT(*)FROM employee GROUP BY sex;
SELECT*FROM employee ORDER BY age DESC;
SELECT NAME,COUNT(*)FROM employee GROUP BY NAME;
SELECT*FROM employee WHERE NAME LIKE'张%';
SELECT id,NAME,sex(*)FROM employee WHERE address='北京';
SELECT COUNT(*)FROM employee;
INSERT INTO employee VARCHAR(8,'小名','男',28,'北京');
UPDATE employee SET address='南京'WHERE id=7;
DELETE FROM employee WHERE age>24;