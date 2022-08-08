input.onButtonPressed(Button.A, function () {
    難易度 = 1
    音階 = [
    262,
    294,
    330,
    349,
    392,
    440,
    494,
    523
    ]
    // 腹筋をしている人のイラスト
    basic.showLeds(`
        . . . . .
        . . . . #
        . # . # #
        # . # # .
        . . . . .
        `)
    開始音()
})
// 傾きから腹筋を判断する。回数に合わせて音程と数字を変化させる。
input.onGesture(Gesture.TiltLeft, function () {
    if (0 < 難易度) {
        動き始めの時間 = input.runningTime()
        速さ = 500
        if (回数 < 音階.length) {
            if (難易度 == 1) {
                music.playTone(音階[回数], music.beat(BeatFraction.Whole))
                表示(音階.length - (回数 + 1))
                回数 += 1
            }
        }
        if (回数 < 音階2.length) {
            if (難易度 == 2) {
                music.playMelody(音階2[回数], 速さ)
                表示(音階2.length - (回数 + 1))
                回数 += 1
            }
        }
    }
})
input.onButtonPressed(Button.AB, function () {
    回数 = 0
    難易度 = 0
    basic.showLeds(`
        . # # # .
        . # . # .
        . . # # .
        . . . . .
        . . # . .
        `)
})
input.onButtonPressed(Button.B, function () {
    難易度 = 2
    音階2 = [
    "C - - - - - - - ",
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
    "C - - - - - - - "
    ]
    // 腹筋をしている人のイラスト
    basic.showLeds(`
        . . . . .
        . . . . #
        . # . # #
        # . # # .
        . . . . .
        `)
    開始音()
})
function 表示 (数値: number) {
    if (数値 == 0) {
        music.setTempo(120)
        music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
        basic.showIcon(IconNames.Happy)
    }
    if (数値 == 1) {
        basic.showLeds(`
            . . # . .
            . # # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    }
    if (数値 == 2) {
        basic.showLeds(`
            . # # # .
            . . . # .
            . # # # .
            . # . . .
            . # # # .
            `)
    }
    if (数値 == 3) {
        basic.showLeds(`
            . # # # .
            . . . # .
            . # # # .
            . . . # .
            . # # # .
            `)
    }
    if (数値 == 4) {
        basic.showLeds(`
            . # . # .
            . # . # .
            . # # # .
            . . . # .
            . . . # .
            `)
    }
    if (数値 == 5) {
        basic.showLeds(`
            . # # # .
            . # . . .
            . # # # .
            . . . # .
            . # # # .
            `)
    }
    if (数値 == 6) {
        basic.showLeds(`
            . # # # .
            . # . . .
            . # # # .
            . # . # .
            . # # # .
            `)
    }
    if (数値 == 7) {
        basic.showLeds(`
            . # # # .
            . # . # .
            . . . # .
            . . . # .
            . . . # .
            `)
    }
    if (数値 == 8) {
        basic.showLeds(`
            . # # # .
            . # . # .
            . # # # .
            . # . # .
            . # # # .
            `)
    }
    if (数値 == 9) {
        basic.showLeds(`
            . # # # .
            . # . # .
            . # # # .
            . . . # .
            . # # # .
            `)
    }
    if (数値 == 10) {
        basic.showLeds(`
            # . # # #
            # . # . #
            # . # . #
            # . # . #
            # . # # #
            `)
    }
    if (数値 == 11) {
        basic.showLeds(`
            # . . # .
            # . . # .
            # . . # .
            # . . # .
            # . . # .
            `)
    }
    if (数値 == 12) {
        basic.showLeds(`
            # . # # #
            # . . . #
            # . # # #
            # . # . .
            # . # # #
            `)
    }
    if (数値 == 13) {
        basic.showLeds(`
            # . # # #
            # . . . #
            # . # # #
            # . . . #
            # . # # #
            `)
    }
    if (数値 == 14) {
        basic.showLeds(`
            # . # . #
            # . # . #
            # . # # #
            # . . . #
            # . . . #
            `)
    }
    if (数値 == 15) {
        basic.showLeds(`
            # . # # #
            # . # . .
            # . # # #
            # . . . #
            # . # # #
            `)
    }
    if (数値 == 16) {
        basic.showLeds(`
            # . # # #
            # . # . .
            # . # # #
            # . # . #
            # . # # #
            `)
    }
}
function 開始音 () {
    music.setVolume(21)
    music.playMelody("G - G - G - C5 - ", 120)
    music.rest(music.beat(BeatFraction.Whole))
}
let 音階2: string[] = []
let 速さ = 0
let 動き始めの時間 = 0
let 音階: number[] = []
let 回数 = 0
let 難易度 = 0
難易度 = 0
let 時間 = 0
回数 = 0
basic.showLeds(`
    . # # # .
    . # . # .
    . . # # .
    . . . . .
    . . # . .
    `)
