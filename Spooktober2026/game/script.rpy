# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Фамильяр")
define me = Character("Ведьманейм")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg myroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    "Утро встретило меня привычной тяжестью поверх одеяла."

    show familiar common with dissolve

    # These display lines of dialogue.

    e "Ведьманейм, просыпайся!"
    e "Ты сама говорила, что у тебя важный день. А уже полдень."

    show familiar sad

    e "Я не хочу, чтобы ты потом ещё 10 лет мне ныла, что ничего не добилась в жизни."
    me "Ладно, ладно. Я бы уже давно встала, если бы ты не давил на меня своим весом."

    # This ends the game.

    return
