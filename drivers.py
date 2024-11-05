import pymysql
connection_established=pymysql.connect(user="root",password='',host='localhost',database="pyth_php")
cursor_setting=connection_established.cursor()

# query='insert into drivers_py values("john",24)'
# query='insert into technical test values("potimao",1,1,63,26,"lewis Hamiliton","portuguesegrandprix","1:29:56.828",2020,"Mercedes","2020-10-23"))'
query='insert into technical test values("portimao",1,63,26,"lewis Hamiliton","1:29:56:828",2020,"mercedes","2020-10-20")'
row=cursor_setting.execute(query)
# data=cursor_setting.fetchall()
# print(data)
