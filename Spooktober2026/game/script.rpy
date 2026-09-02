# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Фамильяр")
define me = Character("Ведьманейм")


#Базовые переменные
default player_resolve = 10
default max_player_resolve = 10
default player_charge = 10
default max_player_charge = 10

#Переменные учёта событий
default room1_2_talk = False

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

    hide familiar
    "И всё же он прав. Впереди большой день. Надо собираться."
    show screen player_stats
    "К счастью, я хорошо выспалась. Я полна решимости, мои силы на максимуме, я со всем справлюсь!"
    "Чтобы провести ритуал сегодня ночью, мне нужны моя книга и карта парка. За каким из предметов отправиться прежде всего?"

    menu: 
        "Куда отправиться в первую очередь?"
        "На чердак, за картой":
            jump room1
        "В подвал, за книгой":
            jump room2



    # This ends the game.

label room1:
    scene bg room1

#Тут фамильяр спросит про ритуал
#    if room1_2_talk == True:
    
    "Так, карта была где-то здесь..."
    with hpunch
    $player_resolve-=1
    "Ай, споткнулась об ящик."
    "О, вот же она, карта."
    show screen map_button

    if room1_2_talk:
        jump tutorial_end
    else:
        $room1_2_talk = True
        "Теперь можно и в подвал"
        jump room2


label room2:
    scene bg room2

    "Так, книга была где-то здесь... Но тут так темно..."
    menu: 
        "Зажечь свет?"
        "Да (Сила: 1)" if player_charge>=1:
            $player_charge -=1
            "Ох, давненько я здесь не прибиралась..."
        "Нет":
            with hpunch
            $player_resolve-=1
            "Ай, споткнулась об ящик."
    "О, вот же она, книга."
    show screen book_button

    if room1_2_talk:
        jump tutorial_end
    else:
        $room1_2_talk = True
        "Теперь можно и на чердак"
        jump room1

label tutorial_end:
 "А теперь можно и отправиться навстречу приключениям."
