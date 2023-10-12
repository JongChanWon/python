import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    
curs = conn.cursor()

e_id = '5'
e_name = '5'
gen = '5'
addr = '5'

sql = f"""insert into emp (e_id, e_name, gen, addr) values('{e_id}', '{e_name}', '{gen}', '{addr}')"""


cnt = curs.execute(sql)
print("cnt", cnt)
conn.commit()

curs.close()
conn.close()