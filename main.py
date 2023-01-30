@namespace
class SpriteKind:
    BOT = SpriteKind.create()
    KEY = SpriteKind.create()
    Door = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    greet()
sprites.on_overlap(SpriteKind.player, SpriteKind.BOT, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_score_by(1)
    KEY2.destroy()
    Jonnsy.say_text("I can finally escape!")
    pause(2000)
    Jonnsy.say_text("i just need to find the door now", 2000, False)
    pause(1000)
sprites.on_overlap(SpriteKind.player, SpriteKind.KEY, on_on_overlap2)

# This function is to tell clue to players where the keys are.
def greet():
    mySprite2.say_text("hi " + name)
    pause(1000)

def on_on_overlap3(sprite3, otherSprite3):
    escapeRoom()
sprites.on_overlap(SpriteKind.player, SpriteKind.Door, on_on_overlap3)

def keyPlacer():
    global KEY2
    KEY2 = sprites.create(img("""
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
        """),
        SpriteKind.KEY)
    KEY2.set_position(40, 295)
def mainCharectar():
    global Jonnsy
    # Don't forget to comment your code as you work!
    Jonnsy = sprites.create(img("""
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
        """),
        SpriteKind.player)
    Jonnsy.set_position(38, 24)
    controller.move_sprite(Jonnsy)
    scene.camera_follow_sprite(Jonnsy)
def escapeRoom():
    global score
    score = info.score()
    if score == 1:
        mySprite.destroy()
        game.set_game_over_message(True, "You have escaped!")
        game.game_over(True)
score = 0
Jonnsy: Sprite = None
KEY2: Sprite = None
mySprite: Sprite = None
mySprite2: Sprite = None
name = ""
tiles.set_current_tilemap(tilemap("""
    level0
"""))
name = game.ask_for_string("What is your name?:)")
info.set_score(0)
mainCharectar()
keyPlacer()
mySprite2 = sprites.create(img("""
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
    """),
    SpriteKind.BOT)
mySprite2.set_position(27, 27)
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.Door)
mySprite.set_position(455, 8)