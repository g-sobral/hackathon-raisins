import sched, time
from datetime import datetime, timedelta
import urllib2
from embedded import Edison
import hackeld_bot as bot

s = sched.scheduler(time.time, time.sleep)
ed = Edison()

def notify(led): 
	urllib2.urlopen("http://192.168.1.129:5000/set/alarm/1/1").read()
	bot.send_telegram_message("O Sr Edison deve tomar o remedio!")
	ed.turn_led_on(led)
	ed.play_buzzer()
	
	# Check button
	check_alarm(led)
	return

def check_alarm(led):

	# Keep pooling button
	start = time.time()
	prev = start
	while not ed.read_button():
		now = time.time()
		late = now - start
		ctrl = now - prev
		if ctrl  > 1:
			urllib2.urlopen("http://192.168.1.129:5000/set/alarm/1/" + 
str(int(late))).read()
			prev = now

	ed.turn_led_off(led)
	bot.send_telegram_message("Remedio Tomado Direitinho ;)")
	urllib2.urlopen("http://192.168.1.129:5000/disable/alarm/1").read()
	return

def start_alarm(delay, led):
	urllib2.urlopen("http://192.168.1.129:5000/set/alarm/1/-1").read()
	s.enter(delay, 1, notify, (led))
	s.run()
	return

def main():
	# Define alarm
	h = 0
	m = 0
	s = 5
	step = 30

	# Setup alarm
	now = datetime.now()
	run_at = now + timedelta(hours=h, minutes=m , seconds=s)
	delay = (run_at - now).total_seconds()

	# Start alarm 1
	start_alarm(delay, 'r')

	# Start alarm 2
	start_alarm(delay + step, 'g')

	# Start alarm 3
	start_alarm(delay + 2*step, 'b')
	return

if __name__ == '__main__':
    main()
