import pymysql

class DaoEmp:
    
    def __init__(self):
        #전역변수로 초기화
        self.conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    # selectList
    def selectList(self):        
        sql = 'SELECT * FROM emp'
        self.curs.execute(sql)
        list = self.curs.fetchall()
        return list
    
    # selectOne
    def selectOne(self, e_id):
        sql = f"""SELECT e_id, e_name, gen, addr FROM emp WHERE e_id= '{e_id}'"""
        self.curs.execute(sql)
        vo = self.curs.fetchone()
        return vo
    
    # insert    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""insert into emp (e_id, e_name, gen, addr) values('{e_id}', '{e_name}', '{gen}', '{addr}')"""
        # 방법1
        # self.curs.execute(sql)
        # cnt = self.curs.rowcount
        
        # 방법2
        cnt = self.curs.execute(sql)
        
        self.conn.commit()
        return cnt
    
    # update
    def update(self, e_id, e_name, gen, addr):
        sql = f"""update emp set e_name='{e_name}', gen='{gen}', addr='{addr}' where e_id ='{e_id}' """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    # delete
    def delete(self, e_id):
        sql = f"delete from emp where e_id='{e_id}'"
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoEmp()
    cnt = de.del_act('6')
    print("cnt",cnt)