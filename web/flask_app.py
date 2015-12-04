#!flask/bin/python
# from flask import Flask, jsonify, request, send_from_directory
from flask import *

app = Flask(__name__)

tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
            },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
            }
        ]

temperature = [
            {
            'temperature': 100,
            }
        ]

datahora = [
        {
        'time': 1,
        'date': True,
        'string': "Hello World"
        }
        ]

# @app.route('/temperatura', methods=['GET'])
# def get_tasks():
    # return jsonify({'temp' : temperatura})

@app.route('/get/date', methods=['GET'])
def get_data():
    return jsonify({'date' : datahora})

@app.route('/get/temperature', methods=['GET'])
def get_temperature():
    return jsonify({'temperature' : temperature})

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    # url_for('/freeboard')
    # url_for('static', filename='freeboard')
    return send_from_directory('freeboard','index.html')
    # return app.send_static_file('freeboard/index.html')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.180')
