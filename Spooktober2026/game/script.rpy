# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Фамильяр")
define me = Character("Ведьманейм")
define bugmage = Character("Жукомагнейм")
define catgirl = Character("Кошканейм")
define coolwitch = Character("Вреднаяведьманейм")
define witchcrowd = Character("Свита")
define eastmage = Character("Старичокнейм")
define geek = Character("Гикнейм")
define notvampire = Character("Тайныймагнейм")
define sceptic = Character("Скептикнейм")
define vampire = Character("Вампирнейм")
define werewolf = Character("Вервольфнейм")


#Базовые переменные
default player_resolve = 10
default max_player_resolve = 10
default player_charge = 10
default max_player_charge = 10

#Переменные учёта событий
default room1_2_talk = False
default entrance_first = True
default have_icecream = False
default have_money = True
default notvampire_first = True

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
jump park_entrance



##########################################
################## АКТ 1 #################
##########################################
################ Локации #################
##########################################





label park_entrance:

    scene bg entrance

    if entrance_first:
        $entrance_first = False
        "Парк выглядит хорошо. Как самый обычный парк. Я боялась столкнуться с призраками прошлого, но нет. Осталось только..."
        "Судя по лёгкому дрожанию воздуха вокруг парка магический барьер."
        "Наставница говорила мне, что внимательность - это главное оружие любой ведьмы, независимо от того, насколько она сильна."
        "Именно внимательность поможет там, где не справятся ни грубая сила, ни магия."
        "Поэтому рассмотрим барьер попристальнее..."
        "Так и знала! Два барьера. Один для отвода глаз простых смертных. Второй - чтобы сдерживать внутри магию и волшебных созданий."
        "Эх, значит ничего не забылось... С другой стороны, будь тут такой барьер в прошлый раз, такимх проблем бы не было."
        "Ладно, хватит стоять на месте. Мой план остаётся прежним:"
        "Сначала найти двух человек к себе в ковен. Хотя бы на сегодня. Затем дождаться ночи и провести ритуал." 
        "В этот раз всё будет в порядке. Я уже не та напуганная девочка, что тринадцать лет назад."

    menu:
        "Ворота призывно ждут."
        "Идти к центральной аллее":
            jump parkroad1
        "Идти к старой беседке":
            jump gazebo


label parkroad1:
    scene bg parkroad1
    menu:
        "Широкая дорога ведёт вглубь парка."
        "Осмотреться":
            "Красиво."
            jump parkroad1
        "Подойти к группе ведьм":
            call t_coolwitch from _call_t_coolwitch
            jump parkroad1
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "Дальше по аллее":
                    jump parkroad2


label parkroad2:
    scene bg parkroad2
    menu:
        "Широкая дорога ведёт вглубь парка. То тут, то там встречаются лавочки."
        "Осмотреться":
            "Красиво."
            jump parkroad2
        "Подойти к странной ведьме":
            call t_catgirl from _call_t_catgirl
            jump parkroad2
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "Назад, ближе ко входу":
                    jump parkroad1
                "К памятному холму":
                    jump hill
                "К кристальной роще":
                    jump crystalwoods
                "К пруду":
                    jump pond
                "К жучиной опушке":
                    jump bugwoods


label hill:
    scene bg hill
    menu:
        "Памятный холм с мемориалом. Тут никого нет."
        "Осмотреться":
            "Красиво."
            jump hill
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "Назад, на аллею":
                    jump parkroad2


label ghosthouse:
    scene bg ghosthouse
    "Серьёзно? Тринадцать лет назад его здесь точно не было, я бы запомнила."
    "Видимо какой-то аттракцион для детишек. Вот только нет ни кассы, ни знаков с инструкциями..."

    menu:
        "Дом с приведениями. Посреди парка. Любопытно."
        "Осмотреть":
            "Красиво."
            jump ghosthouse            
        "Подойти к вампиру":
            call t_vampire from _call_t_vampire
            jump ghosthouse 
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "На жучиную опушку":
                    jump bugwoods


label bugwoods:
    scene bg bugwoods
    menu:
        "Это место привлекает просто огромных жуков."
        "Осмотреться":
            "Красиво."
            jump bugwoods
        "Подойти к мужчине в странной мантии":
            call t_bugmage from _call_t_bugmage
            jump bugwoods
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "К заброшенному дому":
                    jump ghosthouse
                "К центральной аллее":
                    jump parkroad2
                "К старому колоду":
                    jump well


label well:
    scene bg well
    menu:
        "Многие бросали сюда монетки на счастье. Но звука удара об дно не было."
        "Осмотреться":
            "Красиво."
            jump well
        "Подойти к странному парню":
            call t_geek from _call_t_geek
            jump well
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "К жучиной опушке":
                    jump bugwoods


label gazebo:
    scene bg gazebo
    menu:
        "Беседка, которая хорошо укрывала от дождя, даже несмотря на дыры в крыше."
        "Осмотреться":
            "Красиво."
            jump gazebo
        "Подойти к странному парню":
            call t_notvampire from _call_t_notvampire
            jump gazebo
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "К кристальной роще":
                    jump crystalwoods


label crystalwoods:
    scene bg crystalwoods
    menu:
        "Деревья здесь совершенно удивительные."
        "Осмотреться":
            "Красиво."
            jump crystalwoods
        "Подойти к девушке в сером":
            call t_sceptic from _call_t_sceptic
            jump crystalwoods
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "К пруду":
                    jump pond
                "К центральной аллее":
                    jump parkroad2
                "К старой беседке":
                    jump gazebo


label pond:
    scene bg pond
    menu:
        "Иногда в нём проплывают рыбки."
        "Осмотреться":
            "Красиво."
            jump pond
        "Подойти к странному старику":
            call t_eastmage from _call_t_eastmage
            jump pond            
        "Пойти в другое место":
            menu:
                "Куда пойти?"
                "К центральной аллее":
                    jump parkroad2
                "К кристальной роще":
                    jump crystalwoods


##########################################
############### Персонажи ################
##########################################

label t_bugmage:

    show bugmage common

    menu:
        "Мужчина внимательно рассматривает большого жука."
        "Осмотреть":
            "Некрасивый."
            jump t_bugmage
        "Поговорить":
            bugmage "Не беспокой меня, я занят."
            jump t_bugmage
        "Позвать в ковен":
            bugmage "Мне не до глупостей сейчас. Я не вступал в ковен уже двадцать лет."
            jump t_bugmage
        "Отойти":
            hide bugmage
            return


label t_catgirl:

    show catgirl common

    menu:
        "Женщина выглядит довольно изящно и грациозно."
        "Осмотреть":
            "Она одета как ведьма и от неё пахнет магией, но есть в ней что-то странное."
            jump t_catgirl
        "Поговорить":
            catgirl "Мороженое!"
            me "Мороженое?"
            catgirl "Хочу мороженое."
            jump t_catgirl
        "Позвать в ковен":
            catgirl "Мороженое."
            jump t_catgirl
        "Отойти":
            hide catgirl
            return



label t_coolwitch:

    show witchcrowd common
    show coolwitch common


    menu:
        "Девушка со своей свитой стоит так, будто они одни в парке."
        "Осмотреть":
            "Хотела бы я сказать, что она просто пустышка, но магического таланта у неё не отнять."
            jump t_coolwitch
        "Поговорить":
            coolwitch "О! Девочки. Посмотрите кто здесь. Это та самая мухоморная ведьма. Помните тот случай тринадцать лет назад?"
            witchcrowd "Ха ха ха ха ха ха ха!"
            jump t_coolwitch
        "Позвать в ковен":
            coolwitch "Ой, как это мило. Вступить к тебе в ковен. Я обязательно подумаю над этим предложением."
            witchcrowd "Хо хо хо хо хо хо хо!"
            jump t_coolwitch
        "Отойти":
            hide coolwitch
            hide witchcrowd
            return



label t_eastmage:

    show eastmage common

    menu:
        "Старик медитирует у пруда. Он излучает огромную мощь."
        "Осмотреть":
            "Хотела бы я быть такой же могущественной в старости."
            jump t_eastmage
        "Поговорить":
            eastmage "Я знаю, зачем ты пришла. Но не знаю, что тебе сказать."
            jump t_eastmage
        "Позвать в ковен":
            eastmage "Беды. Грядут большие беды."
            jump t_eastmage
        "Отойти":
            hide eastmage
            return



label t_geek:

    show geek common

    menu:
        "Парень бросает монетки, что-то бормочет и записывает в блокнот"
        "Осмотреть":
            "Он выглядит самым обычным человеком. Хотя нет. Он выглядит слишком гиперактивным человеком."
            jump t_geek
        "Поговорить":
            geek "Представляешь? Если бросить монетку в колодец, то нет никакого звука. Наверняка в этом есть какая-то загадка."
            jump t_geek
        "Позвать в ковен":
            geek "Ковен? Ведьмы? Я знал, что они настоящие! Конечно, вступлю! Куда идти? Что делать?"
            jump t_geek
        "Отойти":
            hide geek
            return



label t_notvampire:

    show notvampire common

    if notvampire_first:
        $notvampire_first = False
        notvampire "бу!"
        me "Ты совсем не страшный. И я тебя видела."
        notvampire "бла бла бла..."

    menu:
        "Он красив и совсем не похож на вампира."
        "Осмотреть":
            "Кажется у него один зуб скоро отвалится. Сказать или не сказать?"
            jump t_notvampire
        "Поговорить":
            notvampire "Какими судьбами здесь, ведьма? Захотела дать мне отведать своей кровушки?"
            jump t_notvampire
        "Позвать в ковен":
            notvampire "Я бы с радостью, но у меня есть одно дело. Ты случайно не встречала в парке другого вампира?"
            jump t_notvampire
        "Отойти":
            hide notvampire
            return



label t_sceptic:

    show sceptic common

    menu:
        "Девушка пытается отломать от дерева один из кристаллов."
        "Осмотреть":
            "Она выглядит так, как будто решила убрать из своей жизни все яркие краски."
            jump t_sceptic
        "Поговорить":
            sceptic "Я докажу им всем, что это обычные кристаллы, что это странный, но естественный процесс, что тут нет никакой магии."
            jump t_sceptic
        "Позвать в ковен":
            sceptic "Ещё одна заблудшая душа. Ведьм не существует и я тебе это докажу. У меня как раз есть свободный вечер."
            jump t_sceptic
        "Отойти":
            hide sceptic
            return



label t_vampire:

    show vampire common at left
    show werewolf common at right

    menu:
        "Вампир у дверей и вервольф на балкончике. Ругаются как кошка с собакой."
        "Осмотреть":
            "Та ещё перебранка."
            jump t_vampire
        "Поговорить":
            vampire "Смертная леди, прошу вас об одолжении. Зайдите внутрь и позовите меня внутрь"
            werewolf "Не смей! Если сделаешь это, я тебя из под земли достану. Я запомнил твой запах!"
            jump t_vampire
        "Позвать в ковен":
            vampire "Мои мысли сейчас заняты другой проблемой. Решите её и мы поговорим."
            jump t_vampire
        "Отойти":
            hide vampire
            hide werewolf
            return





##########################################
################## Антракт 1 #################
##########################################
################ Фамильяр #################
##########################################