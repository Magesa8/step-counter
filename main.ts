input.onButtonPressed(Button.A, function () {
    basic.showString("Feet:")
    basic.showNumber(1.5 * Steps)
})
input.onGesture(Gesture.Shake, function () {
    Steps += 2
    basic.showNumber(Steps)
    if (Steps == 6) {
        music.playMelody("E D G F B A C5 B ", 120)
    }
})
let Steps = 0
Steps = 0
