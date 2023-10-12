import pymysql

def dbconnect():
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    return conn
    
def insert_data(conn):
    cur = conn.cursor()
    e_id = input('등록할 사용자의 id를 입력해주세요')
    e_name = input('등록할 사용자의 이름을 입력해주세요')
    gen = input('등록할 사용자의 성별을 입력해주세요')
    addr = input('등록할 사용자의 주소를 입력해주세요')
    sql = "INSERT INTO emp (e_id, e_name, gen, addr) VALUES('" + e_id +"', '" + e_name +"', '" + gen +"', '" + addr +"')"
    
    # sql = """insert into emp (e_id, e_name, gen, addr) values(%s, %s, %s, %s)""" 이렇게 쓰면 전부 스트링으로 인식
    cur.execute(sql)
    conn.commit()
    
def main():
    conn = dbconnect()
    print('연결완료')
    insert_data(conn)
    conn.close()
    print('연결 해제')
    
if __name__ == '__main__':
    main()