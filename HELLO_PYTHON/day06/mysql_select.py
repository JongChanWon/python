import pymysql

def dbconnect():
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    return conn

def search_data(conn):
    cur = conn.cursor(pymysql.cursors.DictCursor) #dictional: json처럼 출력해줌
    sql = 'SELECT * FROM emp'
    cur.execute(sql)
    results = cur.fetchall()
    print(results)
    
def main():
    conn = dbconnect()
    print('연결완료')
    search_data(conn)
    conn.close()
    print('연결 해제')
    
if __name__ == '__main__':
    main()