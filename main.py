def on_button_pressed_a():
    global 難易度, 音階
    難易度 = 1
    音階 = [262, 294, 330, 349, 392, 440, 494, 523]
    # 腹筋をしている人のイラスト
    basic.show_leds("""
        . . . . .
                . . . . #
                . # . # #
                # . # # .
                . . . . .
    """)
    開始音()
input.on_button_pressed(Button.A, on_button_pressed_a)

# 傾きから腹筋を判断する。回数に合わせて音程と数字を変化させる。

def on_gesture_tilt_left():
    global 動き始めの時間, 速さ, 回数
    if 0 < 難易度:
        動き始めの時間 = input.running_time()
        速さ = 500
        if 回数 < len(音階):
            if 難易度 == 1:
                music.play_tone(音階[回数], music.beat(BeatFraction.WHOLE))
                表示(len(音階) - (回数 + 1))
                回数 += 1
        if 回数 < len(音階2):
            if 難易度 == 2:
                music.play_melody(音階2[回数], 速さ)
                表示(len(音階2) - (回数 + 1))
                回数 += 1
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    global 回数, 難易度
    回数 = 0
    難易度 = 0
    basic.show_leds("""
        . # # # .
                . # . # .
                . . # # .
                . . . . .
                . . # . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global 難易度, 音階2
    難易度 = 2
    音階2 = ["C - - - - - - - ",
        "D - F - E - D - ",
        "G - - - G - - - ",
        "G - A - E - F - ",
        "D - - - D - - - ",
        "D - F - E - D - ",
        "C - C5 - B - A - ",
        "G - F - E - D - ",
        "C - - - - - - - ",
        "D - F - E - D - ",
        "G - - - G - - - ",
        "G - A - E - F - ",
        "D - - - D - - - ",
        "D - F - E - D - ",
        "C - G - D - E - ",
        "C - - - - - - - "]
    # 腹筋をしている人のイラスト
    basic.show_leds("""
        . . . . .
                . . . . #
                . # . # #
                # . # # .
                . . . . .
    """)
    開始音()
input.on_button_pressed(Button.B, on_button_pressed_b)

def 表示(数値: number):
    if 数値 == 0:
        music.set_tempo(120)
        music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
        basic.show_icon(IconNames.HAPPY)
    if 数値 == 1:
        basic.show_leds("""
            . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
    if 数値 == 2:
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . # # # .
                        . # . . .
                        . # # # .
        """)
    if 数値 == 3:
        basic.show_leds("""
            . # # # .
                        . . . # .
                        . # # # .
                        . . . # .
                        . # # # .
        """)
    if 数値 == 4:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . # # # .
                        . . . # .
                        . . . # .
        """)
    if 数値 == 5:
        basic.show_leds("""
            . # # # .
                        . # . . .
                        . # # # .
                        . . . # .
                        . # # # .
        """)
    if 数値 == 6:
        basic.show_leds("""
            . # # # .
                        . # . . .
                        . # # # .
                        . # . # .
                        . # # # .
        """)
    if 数値 == 7:
        basic.show_leds("""
            . # # # .
                        . # . # .
                        . . . # .
                        . . . # .
                        . . . # .
        """)
    if 数値 == 8:
        basic.show_leds("""
            . # # # .
                        . # . # .
                        . # # # .
                        . # . # .
                        . # # # .
        """)
    if 数値 == 9:
        basic.show_leds("""
            . # # # .
                        . # . # .
                        . # # # .
                        . . . # .
                        . # # # .
        """)
    if 数値 == 10:
        basic.show_leds("""
            # . # # #
                        # . # . #
                        # . # . #
                        # . # . #
                        # . # # #
        """)
    if 数値 == 11:
        basic.show_leds("""
            # . . # .
                        # . . # .
                        # . . # .
                        # . . # .
                        # . . # .
        """)
    if 数値 == 12:
        basic.show_leds("""
            # . # # #
                        # . . . #
                        # . # # #
                        # . # . .
                        # . # # #
        """)
    if 数値 == 13:
        basic.show_leds("""
            # . # # #
                        # . . . #
                        # . # # #
                        # . . . #
                        # . # # #
        """)
    if 数値 == 14:
        basic.show_leds("""
            # . # . #
                        # . # . #
                        # . # # #
                        # . . . #
                        # . . . #
        """)
    if 数値 == 15:
        basic.show_leds("""
            # . # # #
                        # . # . .
                        # . # # #
                        # . . . #
                        # . # # #
        """)
    if 数値 == 16:
        basic.show_leds("""
            # . # # #
                        # . # . .
                        # . # # #
                        # . # . #
                        # . # # #
        """)
def 開始音():
    music.set_volume(21)
    music.play_melody("G - G - G - C5 - ", 120)
    music.rest(music.beat(BeatFraction.WHOLE))
音階2: List[str] = []
速さ = 0
動き始めの時間 = 0
音階: List[number] = []
回数 = 0
難易度 = 0
難易度 = 0
時間 = 0
回数 = 0
basic.show_leds("""
    . # # # .
        . # . # .
        . . # # .
        . . . . .
        . . # . .
""")