walk = 0

def on_button_pressed_a():
    global walk
    walk = 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def Yellow():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 1023)
def Green():
    pins.analog_write_pin(AnalogPin.P0, 1023)
    pins.analog_write_pin(AnalogPin.P1, 0)
    pins.analog_write_pin(AnalogPin.P2, 1023)
def Red():
    pins.analog_write_pin(AnalogPin.P0, 0)
    pins.analog_write_pin(AnalogPin.P1, 1023)
    pins.analog_write_pin(AnalogPin.P2, 1023)

def on_forever():
    global walk
    walk = 0
    Green()
    basic.pause(4000)
    Yellow()
    basic.pause(1000)
    Red()
    if walk == 1:
        basic.show_leds("""
            # . . . #
                        # . . . #
                        # . # . #
                        . # . # .
                        . . . . .
        """)
    basic.pause(5000)
basic.forever(on_forever)
