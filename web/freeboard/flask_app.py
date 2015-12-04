#!flask/bin/python
# from flask import Flask, jsonify, request, send_from_directory
from flask import *
import random

app = Flask(__name__,static_folder='',static_url_path='')

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
            'temperature': "22."+str(random.randint(1, 9))+" C",
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
    # return send_from_directory('','index.html')
    # return send_from_directory(app.static_folder, 'index.html')
    return app.send_static_file('index.html')
    # return url_for('static', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.180')
