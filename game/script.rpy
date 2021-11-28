# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pov = Character("[povname]",who_color="#ffffff")
define r = Character("Reimu",who_color="#ea4435")
define m = Character("Marisa",who_color="#ffd966")
define y = Character("Yukari",who_color="#c455ff")
define s = Character("Sakuya",who_color="#4284f5")
define rei = Character("Reisen",who_color="#8e7cc3")
define c = Character("Cirno",who_color="#00ffff")
# define u = Character("Utsuho",who_color="#1bd14c")
define k = Character("Kakkoi",who_color="#e1c699")
define e = Character("Eirin",who_color="#1c4587")
define gg = Character("Gregton Grey",who_color="#616161")
define jp = Character("Jesser Purpleman",who_color="#a600ff")
define rem = Character("Remilia",who_color="#b30051")
define g = Character("Granny")
define o = Character("Utsuho",who_color="#1bd14c")

define fade = Fade(2.0, 0.0, 0.0)
define fade2 = Fade(0.0, 0.5, 2.0, color="#000")
define farleft = Position(xpos=0.25)

image yukariNormal = im.Scale("yukari normal.png", 1738/2, 2240/2)
image yukariClosed = im.Scale("yukari frown.png", 1738/2, 2240/2)
image yukariShocked = im.Scale("yukari shocked.png", 1738/2, 2240/2)
image reimuAngry = im.Scale("reimu angry 1.png", 1000, 1000)
image reimuAngryOrbs = im.Scale("reimu angry 2.png", 1000, 1000)
image reimuConfused = im.Scale("reimu confused.png", 1000, 1000)
image reimuNormal = im.Scale("reimu normal.png", 1000, 1000)
image reimuClosed = im.Scale("reimu eyes closed.png", 1000, 1000)
image kakkoiNormal =   im.Scale("kakkoi point.png", 1000, 1000)
image okuuNormal = im.Scale("okuu kill you.png", 6160/3.84, 1000)
image mega = im.Scale("title screen.png", 7595/5.4, 4548/5.4)

#who_color="#6f52ff"
# The game starts here.

label start:
    stop music fadeout 1.0
    
    
    # play music "audio/billiards.mp3"
    play music "<loop 1>audio/billiards.mp3"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    
    scene bg grasslands
    
   
    show okuuNormal at farleft
    show kakkoiNormal at right

    pause 90
    # scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    python:
        povname = renpy.input("What is your name?", length=32)
        povname = povname.strip()

        if not povname:
             povname = "Mario Jones"
    
    
    # These display lines of dialogue.

    pov "Ah good morning! And to all who inhabit it!"


    show yukariNormal:
        alpha 0.0 xalign 0.5 yalign 0
        linear 2 alpha 1.0 xalign 0.5

    pause 2.0
    
    y "Hey"

    pov "Who tf are you?"

    pov "I'm the story's plot hook."

    pov "You have a funny hat. Can I have it?"

    hide yukariNormal

    show yukariClosed

    y "{cps=1.5}...{/cps}"

    hide yukariClosed

    show yukariNormal

    y "I have a better question: Would you like to enther this gap?"

    pov "What Why are there eyes in there?"
    
    pov "Can they help you see faster?"

    hide yukariNormal

    show yukariClosed

    $ renpy.pause(delay=1.5, hard=False)

    pov "Slower then"

    y "{cps=1.5}...{/cps}"

    pov "Sounds like you got some stasis eyes—"

    hide yukariClosed

    show yukariNormal

    y "Would you like to enter this magical world called Gensokyo?"

    y "There are funny fairies and Youkai and you can get powers and meet cool people."

    y "I think you're a…decisive person, so I don’t expect you’ll have any trouble deciding what to do." 
    
    y "If you’re interested, just step into the gap and I will take that as a yes."

    pov "No"

    hide yukariNormal

    show yukariShocked

    y "What?"
    
    pov "My mom told me to say no to entering women’s gaps"
    
    hide yukariShocked

    show yukariNormal

    y "But it's cool."

    pov "I don't like the cold"

    hide yukariNormal

    show yukariShocked

    y "Wh—"

    pov "Time to brush my teth"

    pov "{i}*brushes teeth*{/i}"

    y "It's an adventure of a lifetime—"

    pov "{i}*gargles*{/i}"

    hide yukariShocked

    show yukariNormal

    y "You can get laid!"

    pov "PTOOO no i use the internet i'm practically infertile"

    hide yukariNormal

    show yukariClosed

    y "{cps=1.5}...{/cps}" 

    y "Look…"

    # *tries to convince him more*

    y "Enter this portal to Gensokyo, all of your wildest dreams will come true in this magical land of wonders!"

    pov "No, but can i interest you in some silly string" 
    
    hide yukariClosed

    show yukariShocked

    y "God DAMNIT!"
    
    hide yukariShocked with dissolve
    
    g "SON. WHATS ALL THAT NOOIIISE UP THERE."
    
    g "OOH I CANT STAND ALL THAT NOISEIM WATCHING THE NOSTALGIA CRITIC"

    pov "It’s fine mom, I’m going to school now!"

    g "YEAH YOU BETTAH, LEST YOU MEET THE BLUNT END OF MY CANE."

    hide bg bedroom

    stop music fadeout 1.0
        
    show black
    with fade

    scene bg city
    with fade2

    play music "<loop 32>audio/construction zone.mp3"
    
    pov "Man this is such a long commute"
        
    pov "Buses and trains are closed today"

    pov "But hey at least it’s not like what every grandpa says his commute was like"
    
    pov "mf walking miles scaling mountains going to the mariana trench fighting wolves"
    
    pov "at least with my commute nothing crazy happens"

    # Iovino walks in a city street when he comes across an alleyway with two men

    show gregton at left with moveinright

    show jesser at right with moveinleft

    gg "Hey kid would you like—"
    
menu:
    jp "YO YO YO WANNA GET DRUGS?"

    "DRUGS!? SAY NO THE DRUGS!":

        pov "DRUGS!? SAY NO TO THE DRUG!"

        jump contineud

    "Hell yeah boy gimme some of that mary jane":
        
        pov "Hell yeah boy gimme some of that mary jane."

        jump contineud    

label contineud:  

    gg "No uh he meant to say cotton candy"
    
    pov "Ooh candy!"

    pov "{i}*devours the substance instantaneously*{/i}"

    stop music 
    
    pov "{i}*vanishes*{/i}" 

    play sound "audio/warp.mp3"

    show black
    with fade

    window hide # beat

    pause 2.5 

    window show

    gg "What the fuck." 
    
    gg "Jesser that wasent even meth that was actually just cotton candy why did he just vanish?"

    pov "I don’t think that was cotton candy"

    show black

    play sound "audio/undertald.mp3 "

    show mega:
        alpha 0.0 xalign 0.5 yalign 0.5
        linear 2.5 alpha 1.0 xalign 0.5 yalign 0.5

    pause 5
    
    scene bg forest
    with fade2

    play music "<loop 0>audio/forest part b.mp3"
    
    pov "Should have never smoked that shit now I’m in some fuckin wonderland wizard of oz place"
    
    pov "Hold up wtf is that?"

    stop music fadeout 2

    pause 2
    
    $ renpy.movie_cutscene("forest.mkv", delay=None, loops=0, stop_music=True)

    play music "<loop 0>audio/forest part a.mp3"
    
    scene bg forest

    pov "That was so fucking metal"

    "???" "Another Youkai?"

    pov "Did I just hear someone talking about yogurt what’s going on"

    pov "HEY DOES ANYONE HAVE YOGURT!?" 

    show reimuAngry with moveinleft

    "???" "Stupid Youkai!"
    
    "???" "I will kill you with My huge fucking balls"
    
    hide reimuAngry
    show reimuAngryOrbs

    "???" "My Yin and Yang orbs"
    
    pov "Omg sans undertale can i have autograph"

    hide reimuAngryOrbs
    show reimuConfused

    "???" "What?"

    pov "Who tf are you I just teleported here"

    hide reimuConfused

    show reimuClosed

    "???" "...ah...I guess you must be an outsider"

    r "My name is Reimu, Come with me to the shrine"

    pov "The hell are you on about?"

    hide bg room
    
    show black
    with fade

    pause 2

    scene bg shrine

    pov "Wow!"

    pov "What the hell is this!"

    show reimuNormal at left with moveinleft

    r "Welcome to the Hakurei Shrine, the border between worlds"

    pov "The fuck"

    show marisaHappy at right with moveinright

    m "Hey Reimu"

    hide marisaHappy
    show marisaNormal at right
    
    m "Whos this"
    
    r "An outsider i just found in the forest, they were about to be eaten by a Youkai"

    pov "Yeah these people are probably stoned out of their minds i'm gonna try get their phone call an uber and gtfo of here"
    
    pov "Hey you seem like a pretty funny person on weed can i have your number"
    
    r "Eh? Number?"

    pov "No letter OF COURSE NUMBER ON YOUR PHONE"

    r "A phone? What the heck is that?"

    m "Ah! That's right! Reimu, do you remember Yukari talking about these things that you can use to talk to someone, who is very far away?"

    pov "Are you people are fucking stupid?"

    r "Vaguely…oh! Isn’t it that little box you can bring up to your mouth and you can hear your friends in your ear?"

    pov "I'm going to throw up these people are insane"

    m "Reimu, your friends looking a bit queasy there."

    pov "The end of civilization: no phones...  its just like the boomers predicted"
    
    m "I think they're gonna pass out"

    pov "Im sure this is all a dream and ill wake up bleeding in a ditch"

    r "This isn't a dream"

    pov "Ok then where am I?"

    r "You’re in Gensokyo, Japan"

    pov "Oh thank god i thought this was the Balkans. You scared me there for a second"

    window hide

    pause 5

    window show

    pov "I don't know what a Gensokyo is but let me get this straight real quick Marisa"

    pov "So you’re a witch ok so is it true that you wizards have console wars like magic mirror vs crystal orb"

    hide marisaNormal
    show marisaConfused at right

    m "I have a cauldron"

    m "Cauldron users when their spell rate falls below 6 abracadabras per hocus pocus"

    hide marisaConfused

    show marisaAngry at right

    m "Hey now don’t talk about my motherfuckin cauldron like that"
    
    pov "i bet you make fruit loops in it"

    hide marisaAngry

    show marisaHappy at right

    m "I'm going to kill this guy!"

    hide reimuNormal

    show reimuClosed at left

    r "So glad to see everyones getting along"

    pov "Wait this is japan HOW DO YOU GUYS KNOW PERFECT ENGLISH BUT DONT KNOW WHAT A PHONE IS"

    r "We learned english from all the kids being teleported in here in recent years too many fanfics nowadays"

    m "What are doing talking here?"
    
    m "We still have that incident to resolve you know"

    r "That’s right"
    
    r "Ok [povname] do us a favour"
    
    pov "What"

    r "Go to the Scarlet Devil Mansion; ask the boss there if they know whats up"
    
    pov "The sky"
    
    r "Shut up"

    stop music fadeout 2

    show black
    with fade

    scene bg mansion
    with fade2

    play music "<loop 15>audio/scarlet devil hotel.mp3"
    
    "Some time later..."

    pov "This place has terrible security the guard was sleeping on the job"

    show sakuyaNormal with moveinleft
    
    "???" "Welcome to the scarlet devil mansion, what brings you here?"

    pov "I’m here to see the boss"
    
    "???" "The mistress? A human doesn’t come to the scarlet devil mansion for leisure, I’m assuming it’s important business"

    pov "Assumed correctly"

    s "Very well. I am sakuya, the mistress’s head maid"
    
    pov "Wow! She’s so imdportant even her head has it’s own maid!"
    
    s "Are you like this with everyone"
    
    pov "Yes"

    s "Uh oh"

    scene bg insideMansion
    with fade2

    show sakuyaNormal at left with moveinleft

    show remiliaNormal at right with moveinright

    pov "Holy shit its count dracula"

    r "So this is the human that entered recently?"

    s "It would appear so."
    
    r "Sakuya, give us something to drink."

    s "Yes mistress"

menu:
    s "[povname] Coffee or Tea?"

    "Coffee":
    
        pov "Coffee"

        $ coffe = True

        jump contineud1
        
    "Tea":

        pov "Tea"

        $ coffe = False

        jump contineud1

label contineud1: 
    if coffe:

        s "Wrong it's Tea"
    
    else:
        
        s "Wrong it's Coffee"

    s "Coffee or tea, mistress?"

    r "So tell me, why exactly are you here?"

    pov "Crackheads telling me about an evil person"
    
    r "I see"

    r "Well that doesnt really whittle it down so I really can’t help you"

    r "Why don’t you check the library?"

    pov "Your library is full of just Weird Al album records"
    
    r "A wise man once said that \"{i}He who is tired of Weird Al is tired of life{/i}\", you know"
    
    pov "How do you people not know what a phone is but you know every single Weird Al album you people are fucking weird "
    
    r "haha get it ok shut up"
    
    pov "ok thats it"

    pov "it’s time to unleash my greatest burn of all time"

    pov "yo momma"
    
    pov "so ⑨"
    
    hide remiliaNormal 

    show remiliaAhAhAh at right
    
    r "ONE DEAD HUMAN AH AH AH"
    
    pov "ok its time to gtfo"

    stop music fadeout 2.0

    scene bg grasslands

    show reimuNormal at left with moveinleft

    show marisaNormal at right with moveinright

    r "What did she say?"
    
    pov "She talked about Weird Al"

    hide reimuNormal

    show reimuClosed at left

    r "Well no luck on that culprit"
    
    m "Wait…who's that?"

    hide reimuClosed with moveoutleft

    hide marisaNormal with moveoutleft 
    
    play music "<loop 0>audio/kakkoi.mp3"

    show okuuNormal at left with moveinright

    show kakkoiNormal at right with moveinright

    k "And he says, \"whaddya gonna do now, tough guy?\""
    
    k "And I tell him, \"hey; if you’re gonna put oreos on a pizza\"" 

    hide okuuNormal

    show okuuSmoking at left

    o "At least have some milk to go with it!"

    hide okuuSmoking

    show okuuHappy at left

    o "Cool story can I have some oreos?"

    hide kakkoiNormal

    show kakkoiUnhappy at right

    k "Wh—"

    k "This is the seventh time today youve asked me that."

    hide okuuHappy

    show okuuNormal at left
    
    o "So give me seven oreos."

    k "Shut up."

    pov "I think I found the three stooges minus one"

    hide kakkoiUnhappy

    show kakkoiNormal at right

    k "Well well well. What do we have here?" 

    hide kakkoiNormal

    show kakkoiUnhappy at right

    k "No really, who are these guys?"

    show okuuNormal at center with move

    show reimuNormal at left with moveinleft

    m "I have never seen you before in my life."

    hide kakkoiUnhappy

    show kakkoiSmoking at right

    k "Yeah"

    k "The name’s Kakkoi elbertson and she’s Utsuho ok now tell me yours."

    r "Hello, I’m Reimu."

    m "I’m Marisa"

    hide kakkoiSmoking

    show kakkoiNormal at right

    k "Marisa more like marishart haha yet another hilarious joke."

    o "haha nice one boss"
    
    pov "So Utsuho are you just this persons posse?"

    hide okuuNormal

    show okuuHappy at center

    o "I am the sun god!"

    hide okuuHappy

    show okuuNormal at center 
    
    o "Perhaps!" 

    pov "Perhaps you tweakin"

    hide okuuNormal

    show okuuHappy at center
    
    o "Tweak tweak!"

    hide kakkoiNormal

    show kakkoiUnhappy at right

    k "Ok that’s enough you can tweak on your own time but right now I’m paying you to be my muscle!"
    
    pov "I’m afraid to ask but what are you being paid with?"

    o "Peanut shells"

    pov "PEANUT SHELLS"

    hide kakkoiUnhappy

    show kakkoiSmoking at right
    
    k "Only the finest in Gensokyo!"

    r "Who are you anyhow?"
    
    k "Me? Just some gambler, no need to worry."

    hide kakkoiSmoking

    show kakkoiNormal at right

    k "Though I do have a super cool and interesting backstory."

    m "Can we hear it?"

    hide kakkoiNormal

    show kakkoiSmoking at right

    k "No"

    hide reimuNormal
    show reimuAngry at left

    r "I’m assuming youre the ones behind the incident."

    hide kakkoiSmoking

    show kakkoiNormal at right

    k "No we’re just gonna make the planet green."

    hide reimuAngry

    show reimuNormal at left

    r "Recycling"

    hide reimuNormal

    show reimuClosed at left

    r "Oh phew I thought you were gonna say—"

    hide kakkoiNormal

    show kakkoiSus at right

    k "Green with FAT STACKS OF COLD HARD CASH"
    
    pov "Of course of fucking course"

    hide reimuClosed

    show reimuNormal at left

    r "So you’re going to turn the planet into pure money?"

    hide kakkoiSus

    show kakkoiNormal at right
    
    k "yyyyyep!"

    # Marisa (shocked):

    m "If you do that people will die!"

    hide kakkoiNormal

    show kakkoiSmoking at right
    
    k "So? A little homicide never hurt nobody"

    hide reimuNormal

    show reimuAngry at left
    
    r "That will destroy the planet!"

    pov "Oh no *beat*" 

menu:

    "This has a chance of resulting in a notable decrease in the future voter turnout":
    

        jump contineud2
        
    "This will have a negative impact on the real estate value":

        jump contineud2

label contineud2:

    r "THATS WHAT YOURE CONCERNED ABOUT?"

    k "Okuu go start printing out unreasonably large amounts of money ok thx"

    hide okuuHappy
    show okuuConfused at center

    o "How can you print money?"

    hide kakkoiSmoking

    show kakkoiUnhappy at right

    k "With magic idfk"

    hide okuuConfused

    show okuuHappy at center

    o "oh yeah! How can i be so stupid?"

    hide kakkoiUnhappy

    show kakkoiSmoking at right

    k "It comes naturally."

    hide okuuHappy with moveoutright

    show reimuAngry at center with move

    show marisaNormal at left with moveinleft

    r "You’re not doing that on my watch!"

    k "Alright lemme show you the art of the trade."

    k "I will give you three shinky nickels for you to not stop me."

    hide reimuAngry 

    show reimuHappy at center

    r "Make it two and a half, and you have a deal!"

    pov "what"

    k "Art of the trade"

    k "Haha Took me years to think of that"

    hide marisaNormal with moveinleft

    hide reimuHappy with moveinleft

    show okuuNormal at left with moveinright

    pov "Years wasted"

    k "Well, did you do it?"

    o "I have drank 7 terabytes of plutonium."

    k "OKUU YOU IDIOT"

    o "I will drink some more"

    pov "Sounds like you need risk mitigation."

    hide kakkoiSmoking

    show kakkoiUnhappy at right

    k "Oh, a wise guy eh?"

    hide kakkoiUnhappy

    show KakkoiPointing at right

    k "OKUU SEND THIS WACK ASS BITCH TO THE SCOLDING IRON GATES OF HELL AND HAVE THEM DAMNED!!"

    pov "Do you have any skittles?"

    k "WHERE THEIR UNHOLY TORMENT MAY BE A TESTAMENT TO THEIR WRETCHED LIFE AND WICKED WAYS"

    o "what does that mean?"

    hide KakkoiPointing

    show kakkoiSus at right
    
    k "Kill"

    pause 1

    hide kakkoiSus

    show KakkoiPointing at right

    o "oh yeah sorry hang on one sec"

    $ renpy.movie_cutscene("forest.mkv", delay=None, loops=0, stop_music=True)

    # bg eientei

   
    # This ends the game.

    return

    # Programmed with ❤️ by Kenji