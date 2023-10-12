import pymysql

class DaoMember:
    
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor) #dictional: json처럼 출력해줌
    def selectList(self):        
        sql = 'SELECT * FROM member'
        self.curs.execute(sql)
        members = self.curs.fetchall()
        return members
    
    def selectOne(self, m_id):
        sql = f"SELECT * FROM member WHERE m_id={m_id}"
        self.curs.execute(sql)
        member = self.curs.fetchone()
        return member
    
    def insert(self, m_name, tel, email):
        sql = f"INSERT INTO member(m_name, tel, email) VALUES('{m_name}', '{tel}', '{email}')"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def update(self, m_id, m_name, tel, email):
        # """ 3개 붙이면 엔터쳐도 됨 += 대신 씀
        sql = f"""update member 
                     set m_name='{m_name}', 
                            tel='{tel}', 
                          email='{email}' 
                    where m_id ='{m_id}'"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self, m_id):
        sql = f"delete from member where m_id='{m_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    # 소멸자
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    dm = DaoMember()
    cnt = dm.delete('5')
    print('members', cnt)