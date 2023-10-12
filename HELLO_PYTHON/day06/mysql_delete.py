import pymysql

def dbconnect():
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    return conn
    
def delete_data(conn):
    cur = conn.cursor()
    e_id = input('삭제할 사용자의 id를 입력해주세요: ')
    cur.execute("SELECT e_id FROM emp WHERE e_id = '"+ e_id +"'")
    _id = cur.fetchone()
    sql = "DELETE FROM emp WHERE e_id = '" + _id +"'"
    cur.execute(sql)
    conn.commit()
    
def main():
    conn = dbconnect()
    print('연결완료')
    delete_data(conn)
    conn.close()
    print('연결 해제')
    
if __name__ == '__main__':
    main()