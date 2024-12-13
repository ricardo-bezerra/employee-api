from flask import Flask, render_template, request, jsonify
import json


app = Flask(__name__)


# employees = [
#     {
#         "id": 1, 
#         "title": "Python for Dummies", 
#         "author": "John Campanella"
#     }, 
#     {
#         "id": 2, 
#         "title": "Python for Intermediates", 
#         "author": "John Campanella"
#     }, 
#     {
#         "id": 3, 
#         "title": "Python for Experts", 
#         "author": "John Campanella Jr"
#     },
# ]


@app.route('/')
def index():
    return render_template('index.html')


with open('json_files\employees.json', 'r') as data:
    employees = json.load(data)


@app.route('/employees/', methods=['POST'])
def employee_create():
    new_employee = request.get_json()
    employees.append(new_employee)
    return jsonify(employees)


@app.route('/employees/', methods=['GET'])
def employee_get():
    return jsonify(employees)


@app.route('/employees/<int:userId>', methods=['GET'])
def employee_get_id(userId):
    for employee in employees:
        if employee.get('userId') == userId:
            return jsonify(employee)


@app.route('/employees/<int:userId>', methods=['PUT'])
def employee_update_id(userId):
    updated_employee = request.get_json()
    for index, employee in enumerate(employees):
        if employee.get('userId') == userId:
            employees[index].update(updated_employee)
            return jsonify(employees[index])


@app.route('/employees/<int:userId>', methods=['DELETE'])
def employee_delete_id(userId):
    for index, employee in enumerate(employees):
        if employee.get('userId') == userId:
            del employees[index]
    return jsonify(employees)


# app.run(host="127.0.0.1", port=5000, debug=True)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
