import mraa
import time
from math import log


class Edison:

    def __init__(self):

        # configure leds
        led_pins = { 'r': 4, 'g': 3, 'b': 2 }
        self.leds = {}
        for l, p in led_pins.iteritems():
            self.leds[l] = mraa.Gpio(p)
            self.leds[l].dir(mraa.DIR_OUT)

        # configure temperature sensor (LM358)
        self.temp_sensor = mraa.Aio(0)

        # configure touch button
        self.touch_button = mraa.Gpio(8)
        self.touch_button.dir(mraa.DIR_IN)

        # configure buzzer
        self.buzzer = mraa.Gpio(5)
        self.buzzer.dir(mraa.DIR_OUT)


    def turn_led_on(self, l):
        self.leds[l].write(1)

    def turn_led_off(self, l):
        self.leds[l].write(0)

    def read_temperature(self):
        raw_temp = self.temp_sensor.read()

        resistance = (1023.0/raw_temp)-1.0
        resistance = 100000.0*resistance
        temperature = (1.0/(log(resistance/100000.0)/4299.0+1/298.15))-262.15
        return temperature

    def read_button(self):
        return self.touch_button.read()

    def play_buzzer(self):
        for i in range(3):
            self.buzzer.write(1)
            time.sleep(0.1)
            self.buzzer.write(0)
            time.sleep(0.1)


# test
python if __name__ == __main__:

    ed = Edison()

    ed.turn_led_on('r')
    ed.turn_led_on('g')
    ed.turn_led_on('b')

    time.sleep(1.0)

    #ed.play_buzzer()

    ed.turn_led_off('r')
    ed.turn_led_off('g')
    ed.turn_led_off('b')

    while True:
        print 'temperature:', ed.read_temperature()
        print 'touch button:', ed.read_button()
        time.sleep(0.2)
