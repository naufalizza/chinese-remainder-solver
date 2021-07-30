from flask import Flask, request, make_response, jsonify
from cr_module import parse_and_solve

app = Flask("__main__")

@app.route('/')
def index():
    return "Hello World"

@app.route('/solve',methods=["GET"])
def solve():
    res = ""
    try:
        res = parse_and_solve(request.args.get('data'))
    except:
        res = "invalid input!"
    return jsonify({'data':res})

app.run(debug=True,port=5000)
