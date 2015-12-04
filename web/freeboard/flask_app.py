#!flask/bin/python
# from flask import Flask, jsonify, request, send_from_directory
from flask import *
from embedded import Edison

app = Flask(__name__,static_folder='',static_url_path='')

ed = Edison()

@app.route('/get/date', methods=['GET'])
def get_data():
    datahora = [
            {
                'time': 1,
                'date': True,
                'string': "Hello World"
            }
        ]
    return jsonify({'date' : datahora})

@app.route('/get/temperature', methods=['GET'])
def get_temperature():
    t = ed.read_temperature()
    msg = [
            {
                'temperature': '%.2f C' % t,
            }
        ]
    return jsonify(temperature)

alarms = [False]*10

@app.route('/get/alarm/<int:alarm_id>', methods=['GET'])
def get_alarm(alarm_id):
    return jsonify({'alarm' : {'ringing' : alarms[alarm_id]}})

@app.route('/set/alarm/<int:alarm_id>/<action>', methods=['GET'])
def set_alarm(alarm_id,action):
    if action == "ring":
        alarms[alarm_id] = True
        return "Alarm ringing."
    else:
        alarms[alarm_id] = False
        return "Alarm not ringing."

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    # return send_from_directory('','index.html')
    # return send_from_directory(app.static_folder, 'index.html')
    return app.send_static_file('index.html')
    # return url_for('static', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.180')
