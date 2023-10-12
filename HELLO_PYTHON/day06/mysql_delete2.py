import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    
curs = conn.cursor()

e_id = '6'
sql = f"""delete from emp where e_id ='{e_id}' """


curs.execute(sql)
print("cnt", curs.rowcount)
conn.commit()

curs.close()
conn.close()