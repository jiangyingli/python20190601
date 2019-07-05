from 何佳宁 import try2 as kt
'''
val=["1001"]
rows=kt.query("select * from reader where r_code=%s",val)

print(rows)
'''
val=["王二",'r_004']
kt.update("update reader set r_name=%s where r_code=%s ",val)


