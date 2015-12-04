import mraa

led_pins = { 'r': 4, 'g': 3, 'b': 2 }

leds = {}
for l, p in led_pins:
    leds[l] = mraa.Gpio(p)
    leds[l].dir(mraa.DIR_OUT)

def leds_turnon():
    for k, led in leds.iteritems():
        led.write(1)

def leds_turnoff():
    for k, led in leds.iteritems():
        led.write(0)

while True:
    leds_turnon()
    time.sleep(0.1)
    leds_turnoff
    time.sleep(0.1)
