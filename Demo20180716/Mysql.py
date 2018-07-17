# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='Xiaonei99', database='Mysql')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table userDemo (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into userDemo (id, name) values (%s, %s)', ['1', 'Michael'])
cursor.rowcount

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from userDemo where id = %s', ('1',))
values = cursor.fetchall()
print('values:',values)
# 关闭Cursor和Connection:
cursor.close()

conn.close()