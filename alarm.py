import sched, time
from datetime import datetime, timedelta
import urllib2

s = sched.scheduler(time.time, time.sleep)
ed = Edison()

def notify(): 
	urllib2.urlopen("http://192.168.1.129:5000/set/alarm/1/ring").read()

	ed.turn_led_on('r')
	# Check button
	check_alarm()
	return

def check_alarm():

	# Keep pooling button
	now = time.time()
	while not ed.read_button:
        late = time.time() - now 
        if late > 1:
        	urllib2.urlopen("http://192.168.1.129:5000/set/alarm/1/" + str(late)).read()
	ed.turn_led_off('r')
	return

def start_alarm(delay):
	s.enter(delay, 1, notify, ())
	s.run()
	return

def main():
	# Define alarm
	h = 0
	m = 0
	s = 5

	# Setup alarm
	now = datetime.now()
	run_at = now + timedelta(hours=h, minutes=m , seconds=s)
	delay = (run_at - now).total_seconds()

	# Start alarm
	start_alarm(delay)
	return

if __name__ == '__main__':
    main()