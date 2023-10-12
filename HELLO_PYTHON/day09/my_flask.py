from flask import Flask, redirect
from flask.templating import render_template
from day09.daoemp import DaoEmp
from flask.globals import request
from flask.helpers import url_for, flash


app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello JongChan!'

@app.route('/emp_list')
def emp_list():
    empList = DaoEmp().selectList()
    return render_template("emp_list.html", empList=empList)

@app.route('/emp_detail', methods=['GET'])
def emp_detail():
    e_id = request.args.get("e_id") # emp_list에서 파라미터로 보낸 e_id
    emp = DaoEmp().selectOne(e_id)
    return render_template("emp_detail.html", emp=emp)

@app.route('/emp_add', methods=['GET', 'POST'])
def emp_add():
    if request.method == 'GET':
        return render_template("emp_add.html")
    else:
        e_id = request.form['e_id']
        e_name = request.form['e_name']
        gen = request.form['gen']
        addr = request.form['addr']
        cnt = DaoEmp().insert(e_id, e_name, gen, addr)
        if cnt > 0:
            msg = "성공"
        else:
            # flash('이미 존재하는 사용자')
            msg = "실패"
        # return render_template("emp_add_act.html", msg=msg)  
        return redirect(url_for("emp_list"))

@app.route('/emp_mod', methods=['GET', 'POST'])
def emp_mod():
    e_id = request.args.get("e_id")
    emp = DaoEmp().selectOne(e_id)
    if request.method == 'GET':
        return render_template("emp_mod.html", emp=emp)
    elif request.method == 'POST':
        e_id = request.form['e_id']
        e_name = request.form['e_name']
        gen = request.form['gen']
        addr = request.form['addr']
        cnt = DaoEmp().update(e_id, e_name, gen, addr)
        
        if cnt > 0:
            msg = "성공"
        else:
            msg = "실패"
            
        return render_template("emp_mod_act.html", cnt=cnt, msg=msg)

@app.route('/emp_del_act', methods=['POST'])
def emp_del_act():
    e_id = request.form['e_id']
    cnt = DaoEmp().delete(e_id)
    return render_template("emp_mod_act.html", cnt=cnt)

@app.route('/emp_del')
def emp_del():                        
    e_id = request.args.get("e_id")
    cnt = DaoEmp().delete(e_id)
    if cnt > 0:
        msg = "성공"
    else:
        msg = "실패"
    return redirect(url_for("emp_list"))
if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    