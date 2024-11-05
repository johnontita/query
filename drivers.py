import pymysql
connection_established=pymysql.connect(user="root",password='',host='localhost',database="pyth_php")
cursor_setting=connection_established.cursor()


query='insert into technical test values("portimao",1,63,26,"lewis Hamiliton","1:29:56:828",2020,"mercedes","2020-10-20")'
row=cursor_setting.execute(query)

