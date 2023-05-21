let walk = 0
input.onButtonPressed(Button.A, function () {
    walk = 1
})
function Yellow () {
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P14, 0)
    pins.analogWritePin(AnalogPin.P15, 1023)
}
function Green () {
    pins.analogWritePin(AnalogPin.P13, 1023)
    pins.analogWritePin(AnalogPin.P14, 0)
    pins.analogWritePin(AnalogPin.P15, 1023)
}
function Red () {
    pins.analogWritePin(AnalogPin.P13, 0)
    pins.analogWritePin(AnalogPin.P14, 1023)
    pins.analogWritePin(AnalogPin.P15, 1023)
}
basic.forever(function () {
    basic.clearScreen()
    walk = 0
    Green()
    basic.pause(4000)
    Yellow()
    basic.pause(1000)
    Red()
    if (walk == 1) {
        basic.showLeds(`
            # . . . #
            # . . . #
            # . # . #
            . # . # .
            . . . . .
            `)
    }
    basic.pause(5000)
})
