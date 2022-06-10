def on_button_pressed_a():
    basic.show_string("Feet:")
    basic.show_number(1.5 * Steps)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    global Steps
    Steps += 2
    basic.show_number(Steps)
    if Steps == 6:
        music.play_melody("E D G F B A C5 B ", 120)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

Steps = 0
Steps = 0