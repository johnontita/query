import pymysql
connection_established=pymysql.connect(user="root",password='',host='localhost',database="pyth_php")
cursor_setting=connection_established.cursor()
# query=cursor_setting.execute("CREATE TABLE drivers(location VARCHAR,grid INTEGER,position INTEGER,points INTEGERS,driver name VARCHAR,race-name VARCHAR,time INTEGER,year INTEGER,team_name VARCHAR,date INTEGER")
# query_field_one=cursor_setting.execute("INSERT INTO drivers VALUES()")
# data=cursor_setting.fetchall()
# query='select*from drivers_py'
query='insert into drivers_py values("john",24)'
row=cursor_setting.execute(query)
# data=cursor_setting.fetchall()
# print(data)
