import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    
curs = conn.cursor()

e_id = '6'
e_name = '6'
gen = '6'
addr = '6'

sql = f"""insert into emp (e_id, e_name, gen, addr) values('{e_id}', '{e_name}', '{gen}', '{addr}')"""


curs.execute(sql)
print("cnt", curs.rowcount)
conn.commit()

curs.close()
conn.close()