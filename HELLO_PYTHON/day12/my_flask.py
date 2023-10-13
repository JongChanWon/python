from flask import Flask, request, jsonify
from flask.templating import render_template
from day12.daoemp import DaoEmp

app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello JongChan!'

@app.route('/emp_selects', methods=['POST'])
def emp_selects():
    list = DaoEmp().selectList()
    return jsonify({'list':list})

@app.route('/emp_select', methods=['GET'])
def emp_select():
    e_id = request.args.get("e_id")
    one = DaoEmp().selectOne(e_id)
    return jsonify({'one':one})

@app.route('/myajax', methods=['POST', 'GET'])
def myajax():
    
    # menu = request.form['menu']
    menu = request.args.get('menu')
    print(request.form)
    print("menu: ", menu)
    return jsonify({'msg': 'hello'})

@app.route('/myajax_axios', methods=['POST', 'GET'])
def myajax_axios():
    params = request.get_json()
    print("params", params)
    return jsonify({'msg': 'hello'})

if __name__ == '__main__':
    app.run(debug=True)