import mraa
import time
from math import log


class Edison:

    def __init__(self):

        # configure leds
        led_pins = { 'r': 4, 'g': 3, 'b': 2 }
        self.leds = {}
        for l, p in led_pins.iteritems():
            leds[l] = mraa.Gpio(p)
            leds[l].dir(mraa.DIR_OUT)

        # configure temperature sensor (LM358)
        self.temperature = mraa.Aio(0)

    def turn_led_on(self, l):
        self.leds[l].write(1)

    def turn_led_on(self, l):
        self.leds[l].write(0)

    def get_temperature(self):
        raw_temp = self.temperature.read()
        print 'raw_temp:', raw_temp

        resistance = (1023-raw_temp)*10000/raw_temp
        temperature = 1/(log(resistance/10000)/3975+1/298.15)-273.15
        print 'temperature:', temperature

ed = Edison()

ed.turn_led_on('r')
ed.turn_led_on('g')
ed.turn_led_on('b')

ed.get_temperature()
time.sleep(1.0)

ed.turn_led_off('r')
ed.turn_led_off('g')
ed.turn_led_off('b')
