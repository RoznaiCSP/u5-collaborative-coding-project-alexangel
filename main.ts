namespace SpriteKind {
    export const BOT = SpriteKind.create()
    export const KEY = SpriteKind.create()
    export const Door = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.BOT, function (sprite, otherSprite) {
    greet()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.KEY, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    KEY.destroy()
    Jonnsy.sayText("I can finally escape!")
    pause(2000)
    Jonnsy.sayText("i just need to find the door now", 2000, false)
    pause(1000)
})
// This function is to tell clue to players where the keys are.
function greet () {
    mySprite2.sayText("hi " + name)
    pause(1000)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Door, function (sprite, otherSprite) {
    escapeRoom()
})
function keyPlacer () {
    KEY = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . 5 5 5 5 . . . . . . . . . . 
        . . 5 . . 5 5 5 5 5 5 5 5 5 5 . 
        . . 5 . . 5 . . . . 5 . . . 5 . 
        . . 5 5 5 5 . . . . 5 . . . 5 . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.KEY)
    KEY.setPosition(40, 295)
}
function mainCharectar () {
    // Don't forget to comment your code as you work!
    Jonnsy = sprites.create(img`
        . . . . . . . . . . b 5 b . . . 
        . . . . . . . . . b 5 b . . . . 
        . . . . . . b b b b b b . . . . 
        . . . . . b b 5 5 5 5 5 b . . . 
        . . . . b b 5 d 1 f 5 d 4 c . . 
        . . . . b 5 5 1 f f d d 4 4 4 b 
        . . . . b 5 5 d f b 4 4 4 4 b . 
        . . . b d 5 5 5 5 4 4 4 4 b . . 
        . b b d d d 5 5 5 5 5 5 5 b . . 
        b d d d b b b 5 5 5 5 5 5 5 b . 
        c d d b 5 5 d c 5 5 5 5 5 5 b . 
        c b b d 5 d c d 5 5 5 5 5 5 b . 
        c b 5 5 b c d d 5 5 5 5 5 5 b . 
        b b c c c d d d 5 5 5 5 5 d b . 
        . . . . c c d d d 5 5 5 b b . . 
        . . . . . . c c c c c b b . . . 
        `, SpriteKind.Player)
    Jonnsy.setPosition(38, 24)
    controller.moveSprite(Jonnsy)
    scene.cameraFollowSprite(Jonnsy)
}
function escapeRoom () {
    score = info.score()
    if (score == 1) {
        mySprite.destroy()
        game.setGameOverMessage(true, "You have escaped!")
        game.gameOver(true)
    }
}
let score = 0
let Jonnsy: Sprite = null
let KEY: Sprite = null
let mySprite: Sprite = null
let mySprite2: Sprite = null
let name = ""
tiles.setCurrentTilemap(tilemap`level0`)
name = game.askForString("What is your name?:)")
info.setScore(0)
mainCharectar()
keyPlacer()
mySprite2 = sprites.create(img`
    ........................
    .....ffff...............
    ...fff22fff.............
    ..fff2222fff............
    .fffeeeeeefff...........
    .ffe222222eef...........
    .fe2ffffff2ef...........
    .ffffeeeeffff...........
    ffefbf44fbfeff..........
    fee41fddf14eef..........
    .ffffdddddeef...........
    fddddf444eef............
    fbbbbf2222f4e...........
    fbbbbf2222fd4...........
    .fccf45544f44...........
    ..ffffffff..............
    ....ff..ff..............
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    ........................
    `, SpriteKind.BOT)
mySprite2.setPosition(27, 27)
mySprite = sprites.create(img`
    e e e e e e e e e e e e e e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 f f f 
    e e 1 e 1 e 1 e 1 e 1 e 1 f f f 
    e e 1 e 1 e 1 e 1 e 1 e 1 f f f 
    e e 1 e 1 e 1 e 1 e 1 e 1 f f f 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e 1 e 1 e 1 e 1 e 1 e 1 e e e 
    e e e e e e e e e e e e e e e e 
    `, SpriteKind.Door)
mySprite.setPosition(455, 8)
