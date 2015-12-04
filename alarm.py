import sched, time
from datetime import datetime, timedelta
import urllib2

s = sched.scheduler(time.time, time.sleep)
def notify(): 
	urllib2.urlopen("192.168.1.180:5000/").read()
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