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
    return jsonify({'temperature':, msg})

alarms = [False]*10
alarmTimes = [0]*10

@app.route('/disable/alarm/<int:alarm_id>', methods=['GET'])
def disable_alarm(alarm_id):
    alarms[alarm_id] = False
    return ""

@app.route('/get/alarm/<int:alarm_id>', methods=['GET'])
def get_alarm(alarm_id):
    return jsonify({'alarm' : {'ringing' : alarmTimes[alarm_id],
        'enabled' : alarms[alarm_id]
        }})

@app.route('/set/alarm/<int:alarm_id>/<time>', methods=['GET'])
def set_alarm(alarm_id,time):
    alarms[alarm_id] = True
    alarmTimes[alarm_id] = int(time)
    return ""

@app.route('/dashboard', methods=['GET'])
def get_dashboard():
    # return send_from_directory('','index.html')
    # return send_from_directory(app.static_folder, 'index.html')
    return app.send_static_file('index.html')
    # return url_for('static', filename='index.html')


if __name__ == '__main__':
    app.run(debug=True,host='192.168.1.180')
