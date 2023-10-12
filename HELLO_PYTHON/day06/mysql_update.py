import pymysql


conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    
curs = conn.cursor()

e_id = '6'
e_name = '7'
gen = '7'
addr = '7'

sql = f"""update emp set e_name='{e_name}', gen='{gen}', addr='{addr}' where e_id ='{e_id}' """


curs.execute(sql)
print("cnt", curs.rowcount)
conn.commit()

curs.close()
conn.close()