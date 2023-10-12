from flask import Flask, request
from flask.templating import render_template
from astropy.io.misc.yaml import name
import pymysql
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello JongChan!'

@app.route('/param')
def param():
    menu = request.args.get('menu')
    
    return 'param:' + menu

@app.route('/post', methods=['POST', 'GET'])
def post():
    # menu = request.form.get('menu')
    menu = request.form['menu']
    return 'post: ' + menu

@app.route('/forw')
def forw():
    a = '김가영 똥먹기 냠냠'
    b = ['전우치', '이순신', '유관순']
    c = [
            {'e_id': 1, 'e_name': 1, 'gen': 1, 'addr': 1, },
            {'e_id': 2, 'e_name': 2, 'gen': 2, 'addr': 2, },
            {'e_id': 3, 'e_name': 3, 'gen': 3, 'addr': 3, }
        ]
    return render_template("forw.html", a=a, b=b, c=c)

@app.route('/emp')
def emp():
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', password='python', db='python', charset='utf8')
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM emp'
    curs.execute(sql)
    emps = curs.fetchall()
    
    curs.close()
    conn.close()
    
    return render_template("emp.html", emps=emps)

if __name__ == '__main__':
    app.run(debug=True)