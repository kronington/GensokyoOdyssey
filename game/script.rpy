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
define k = Character("Kakkoi",who_color="#e1c699")
define e = Character("Eirin",who_color="#1c4587")
define gg = Character("Gregton Grey",who_color="#616161")
define jp = Character("Jesser Purpleman",who_color="#a600ff")
define rem = Character("Remilia",who_color="#b30051")
define g = Character("Granny")
define o = Character("Utsuho",who_color="#1bd14c")

define fade = Fade(2.0, 0.0, 0.0)
define fade3 = Fade(5.0, 0.0, 0.0)
define fade2 = Fade(0.0, 0.5, 2.0, color="#000")

define farleft = Position(xpos=0.25)
define farfarleft = Position(xpos=0.145)
define farright = Position(xpos=0.84)
define offcentered1 =  Position(xpos=0.367)
define  offcentered = Position(xpos=0.60)

image yukariNormal = im.Scale("yukari normal.png", 1738/2.24, 1000)
image yukariClosed = im.Scale("yukari frown.png", 1738/2.24, 1000)
image yukariShocked = im.Scale("yukari shocked.png", 1738/2.24, 1000)
image reimuAngry = im.Scale("reimu angry 1.png", 3361/3.84, 1000)
image reimuAngryOrbs = im.Scale("reimu angry 2.png", 3361/3.84, 1000)
image reimuConfused = im.Scale("reimu confused.png", 3361/3.84, 1000)
image reimuNormal = im.Scale("reimu normal.png", 3361/3.84, 1000)
image reimuClosed = im.Scale("reimu eyes closed.png", 3361/3.84, 1000)
image reimuHappy = im.Scale("reimu happy.png",3361/3.84,1000)
image gregtonE = im.Scale("gregton.png",787/1.801,1000)
image jesserE = im.Scale("jesser.png",787/1.801,1000)
image eirinConfused = im.Scale("eirin confused.png",2400/3.8,1000)
image eirinClosed = im.Scale("eirin frown.png",2400/3.8,1000)
image eirinNormal = im.Scale("eirin normal.png",2400/3.8,1000)
image eirinHappyClosed = im.Scale("eirin happy closed.png",2400/3.8,1000)
image kakkoiNormal = im.Scale("kakkoi normal.png",3122/3.84,1000)
image kakkoiPointing = im.Scale("kakkoi point.png",3122/3.84,1000)
image kakkoiSmoking = im.Scale("kakkoi smoking it.png",3122/3.84,1000)
image kakkoiSus = im.Scale("kakkoi SUS.png",3122/3.84,1000)
image kakkoiUnhappy = im.Scale("kakkoi unhappy.png",3122/3.84,1000)
image okuuHappy =  im.Scale("okuu happy.png", 3446/3.84, 1000)
image okuuKiller = im.Scale("okuu kill you.png", 6160/3.84, 1000)
image okuuNormal = im.Scale("okuu normal.png", 3446/3.84, 1000)
image okuuConfused = im.Scale("okuu question.png", 3446/3.84, 1000)
image okuuShoot = im.Scale("okuu shoot at you.png", 6160/3.84, 1000)
image remiliaAhAhAh =  im.Scale("remilia ah ah ah.png", 2400/3.8, 1000)
image remiliaNormal = im.Scale("remilia normal.png", 2400/3.8, 1000)
image remiliaAngry = im.Scale("remilia angry.png", 2400/3.8, 1000)
image cirnoFumo = im.Scale("cirno fumo.png", 2400/3.8, 1000)
image cirnoHappy = im.Scale("cirno happy.png", 2400/3.8, 1000)
image cirnoNormal = im.Scale("cirno normal.png", 2400/3.8, 1000)
image marisaAngry = im.Scale("marisa angry.png", 504/0.6, 950)
image marisaConfused = im.Scale("marisa shocked.png", 504/0.539, 950)
image marisaNormal = im.Scale("marisa neutral.png", 504/0.539, 950)
image marisaHappy = im.Scale("marisa happy.png", 504/0.539, 950)
image marisaShocked = im.Scale("marisa shocked.png", 504/0.539, 950)
image sakuyaNormal = im.Scale("sakuya normal.png",1320/2.07,1000)
image reisenConcerned = im.Scale("reisen concerned.png",1320/2.27,1000)
image reisenNormal = im.Scale("reisen normal 2.png",1320/2.27,1000)

image KakkoiPointing2 = im.Scale("kakkoi point.png", 1000, 1000)

image mega = im.Scale("title screen.png", 7595/5.4, 4548/5.4)

#who_color="#6f52ff"
# The game starts here.

label start:
    stop music fadeout 0.5
    
    # play music "audio/billiards.mp3"
    
    
    # show okuuNormal at left

    # show okuuNormal at offcentered with move

    # pause 60

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg bedroom

    pause 0.5

    play music "<loop 1>audio/billiards.mp3" fadein 2.0

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
        alpha 0.0 xalign 0.5 yalign 1.0
        linear 2 alpha 1.0 xalign 0.5

    pause 2.0
    
    y "Hey"

    # Some old testing code
    # show yukariNormal
    # show yukariClosed 
    # show yukariShocked
    # show reimuAngry
    # show reimuAngryOrbs 
    # show reimuConfused 
    # show reimuNormal 
    # show reimuClosed 
    # show reimuHappy 
    # show gregtonE
    # show jesserE 
    # show eirinConfused 
    # show eirinClosed
    # show eirinNormal 
    # show eirinHappyClosed 
    # show kakkoiNormal   
    # show kakkoiPointing 
    # show kakkoiSmoking
    # show kakkoiSus
    # show kakkoiUnhappy
    # show okuuHappy 
    # show okuuKiller 
    # show okuuNormal 
    # show okuuConfused
    # show okuuShoot
    # show remiliaAhAhAh 
    # show remiliaNormal
    # show remiliaAngry 
    # show cirnoFumo 
    # show cirnoHappy 
    # show cirnoNormal
    # show marisaAngry 
    # show marisaConfused 
    # show marisaNormal 
    # show marisaHappy 
    # show sakuyaNormal
    # show reisenConcerned
    # show reisenNormal

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

    pov "Time to brush my teeth"

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

    play music "<loop 32>audio/construction zone.mp3" fadein 2.0
    
    pov "Man this is such a long commute"
        
    pov "Buses and trains are closed today"

    pov "But hey at least it’s not like what every grandpa says his commute was like"
    
    pov "mf walking miles scaling mountains going to the mariana trench fighting wolves"
    
    pov "at least with my commute nothing crazy happens"

    # Iovino walks in a city street when he comes across an alleyway with two men

    show gregtonE at left with moveinright

    show jesserE at right with moveinleft

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

    play sound "audio/warp.mp3"

    stop music fadeout 0.5
    
    # pov "{i}*vanishes*{/i}" 

    

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

    play music "<loop 0>audio/forest part b.mp3" fadein 2.0
    
    pov "Should have never smoked that shit now I’m in some fuckin wonderland wizard of oz place"
    
    pov "Hold up wtf is that?"

    stop music fadeout 2

    pause 2
    
    $ renpy.movie_cutscene("forest.mkv", delay=None, loops=0, stop_music=True)

    play music "<loop 0>audio/forest part a.mp3" fadein 2.0
    
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
    with fade2

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

    pause 2.25

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

    scene bg scarlet devil mansion
    with fade2

    play music "<loop 15>audio/scarlet devil hotel.mp3" fadein 2.0
    
    "Some time later..."

    pov "This place has terrible security the guard was sleeping on the job"

    show sakuyaNormal with moveinleft
    
    "???" "Welcome to the Scarlet Devil Mansion, what brings you here?"

    pov "I’m here to see the boss"
    
    "???" "The mistress? A human doesn’t come to the Scarlet Devil Mansion for leisure, I’m assuming it’s important business"

    pov "Assumed correctly"

    s "Very well. I am Sakuya, the mistress’s head maid"
    
    pov "Wow! She’s so important even her head has it’s own maid!"
    
    s "Are you like this with everyone"
    
    pov "Yes"

    s "Uh oh"

    show black
    with fade

    scene bg scarlet devil mansion:
        xalign 0.54 yalign 0.35 zoom 1.525
    with fade2

    show sakuyaNormal at left with moveinleft

    show remiliaNormal at right with moveinright

    pov "Holy shit its count dracula"

    rem "So this is the human that entered recently?"

    s "It would appear so."
    
    rem  "Sakuya, give us something to drink."

    s "Yes mistress"

menu:
    s "[povname], Coffee or Tea?"

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

        s "Wrong, it's Tea"

        s "Coffee or tea, mistress?"

        rem  "Tea"

        rem "Wrong, it's Coffee"
    
    else:
        
        s "Wrong, it's Coffee"

        s "Coffee or tea, mistress?"

        rem "Coffee"

        rem  "Wrong, it's Tea"


    rem  "So tell me, why exactly are you here?"

    pov "Crackheads telling me about an evil person"
    
    rem "I see"

    rem "Well that doesnt really whittle it down so I really can’t help you"

    rem "Why don’t you check the library?"

    pov "Your library is full of just Weird Al album records"
    
    rem "A wise man once said that \"{i}He who is tired of Weird Al is tired of life{/i}\", you know"
    
    pov "How do you people not know what a phone is but you know every single Weird Al album you people are fucking weird "
    
    rem "haha get it ok shut up"
    
    pov "ok thats it"

    pov "it’s time to unleash my greatest burn of all time"

    pov "yo momma"
    
    pov "so ⑨"
    
    hide remiliaNormal 

    show remiliaAhAhAh at right
    
    rem "ONE DEAD HUMAN AH AH AH"
    
    pov "ok its time to gtfo"

    stop music fadeout 2.0

    show black
    with fade

    scene bg grasslands
    with fade2

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
    
    play music "<loop 0>audio/kakkoi.mp3" fadein 2.0

    show okuuNormal at left with moveinright

    show kakkoiNormal at farright with moveinright

    k "And he says, \"whaddya gonna do now, tough guy?\""
    
    k "And I tell him, \"hey; if you’re gonna put oreos on a pizza\"" 

    hide kakkoiNormal

    show kakkoiSmoking at farright 

    o "At least have some milk to go with it!"

    hide okuuNormal

    show okuuHappy at left

    o "Cool story can I have some oreos?"

    hide kakkoiSmoking

    show kakkoiUnhappy at farright 

    k "Wh—"

    k "This is the seventh time today youve asked me that."

    hide okuuHappy

    show okuuNormal at left
    
    o "So give me seven oreos."

    k "Shut up."

    pov "I think I found the three stooges minus one"

    hide kakkoiUnhappy

    show kakkoiNormal at farright 

    k "Well well well. What do we have here?" 

    hide kakkoiNormal

    show kakkoiUnhappy at farright 

    k "No really, who are these guys?"

    show okuuNormal at offcentered1 with move

    show reimuNormal at farfarleft with moveinleft

    m "I have never seen you before in my life."

    hide kakkoiUnhappy

    show kakkoiSmoking at farright

    k "Yeah"


    k "Ladies and gentlemen of the jury, may i have the attention of the class."
    
    k "My name’s kakkoi elbertson and she’s utsuho ok now tell me yours."

    r "Hello, I’m Reimu."

    m "I’m Marisa"

    hide kakkoiSmoking

    show kakkoiNormal at farright

    k "Marisa more like marishart haha yet another hilarious joke."

    o "haha nice one boss"
    
    pov "So Utsuho are you just this persons posse?"

    hide okuuNormal

    show okuuHappy at offcentered 

    o "I am the sun god!"

    hide okuuHappy

    show okuuNormal at offcentered  
    
    o "Perhaps!" 

    pov "Perhaps you tweakin"

    hide okuuNormal

    show okuuHappy at offcentered 
    
    o "Tweak tweak!"

    hide kakkoiNormal

    show kakkoiUnhappy at farright 

    k "Ok that’s enough you can tweak on your own time but right now I’m paying you to be my muscle!"
    
    pov "I’m afraid to ask but what are you being paid with?"

    o "Peanut shells"

    pov "PEANUT SHELLS"

    hide kakkoiUnhappy

    show kakkoiSmoking at farright 
    
    k "Only the finest in Gensokyo!"

    r "Who are you anyhow?"
    
    k "Me? Just some gambler, no need to worry."

    hide kakkoiSmoking

    show kakkoiNormal at farright 

    k "Though I do have a super cool and interesting backstory."

    m "Can we hear it?"

    hide kakkoiNormal

    show kakkoiSmoking at farright 

    k "No"

    hide reimuNormal
    show reimuAngry at farfarleft

    r "I’m assuming youre the ones behind the incident."

    hide kakkoiSmoking

    show kakkoiNormal at farright 

    k "No we’re just gonna make the planet green."

    hide reimuAngry

    show reimuNormal at farfarleft

    r "Recycling"

    hide reimuNormal

    show reimuClosed at farfarleft

    r "Oh phew I thought you were gonna say—"

    hide kakkoiNormal

    show kakkoiSus at farright 

    k "Green with FAT STACKS OF COLD HARD CASH"
    
    pov "Of course of fucking course"

    hide reimuClosed

    show reimuNormal at farfarleft

    r "So you’re going to turn the planet into pure money?"

    hide kakkoiSus

    show kakkoiNormal at farright 
    
    k "yyyyyep!"

    
    show marisaShocked:
        xalign -2.0 yalign 1.0 rotate 135
        linear 2.5 xalign 0.5 yalign 6.0


    m "If you do that people will die!"

    hide kakkoiNormal

    show kakkoiSmoking at farright 
    
    k "So? A little homicide never hurt nobody"

    hide reimuNormal

    hide marisaShocked

    show reimuAngry at farfarleft
    
    r "That will destroy the planet!"

    pov "Oh no" 

    window hide

    pause 2.25

    window show


menu:
    "Select an option:"

    "This has a chance of resulting in a notable decrease in the future voter turnout":
    

        jump contineud2
        
    "This will have a negative impact on the real estate value":

        jump contineud2

label contineud2:

    r "THATS WHAT YOURE CONCERNED ABOUT?"

    k "Okuu go start printing out unreasonably large amounts of money ok thx"

    hide okuuHappy
    show okuuConfused at offcentered 

    o "How can you print money?"

    hide kakkoiSmoking

    show kakkoiUnhappy at farright 

    k "With magic idfk"

    hide okuuConfused

    show okuuHappy at offcentered 

    o "oh yeah! How can i be so stupid?"

    hide kakkoiUnhappy

    show kakkoiSmoking at farright 

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

    hide marisaNormal with moveoutleft

    hide reimuHappy with moveoutleft

    show okuuNormal at farleft with moveinright

    k "Well, did you do it?"

    o "I have drank 7 terabytes of plutonium."

    k "OKUU YOU IDIOT"

    o "I will drink some more"

    pov "Sounds like you need risk mitigation."

    hide kakkoiSmoking

    show kakkoiUnhappy at farright

    k "Oh, a wise guy eh?"

    hide kakkoiUnhappy

    show kakkoiPointing at farright

    k "OKUU SEND THIS WACK ASS BITCH TO THE SCOLDING IRON GATES OF HELL AND HAVE THEM DAMNED!!"

    pov "Do you have any skittles?"

    k "WHERE THEIR UNHOLY TORMENT MAY BE A TESTAMENT TO THEIR WRETCHED LIFE AND WICKED WAYS"

    o "what does that mean?"

    hide kakkoiPointing

    show kakkoiSus at farright
    
    k "Kill"

    pause 1

    hide okuuNormal

    show okuuKiller at farleft

    hide kakkoiSus

    show kakkoiPointing at farright

    o "oh yeah sorry hang on one sec"

    hide okuuNormal

    show okuuKiller at farleft

    show kakkoiPointing at right

    stop music fadeout 0.0

    $ renpy.movie_cutscene("boom.mkv", delay=None, loops=0, stop_music=True)

    

    scene bg eientei
    with fade2

    play music "<loop 32>audio/construction zone.mp3" fadein 2.0

    show reisenConcerned at left with moveinleft
    show eirinNormal at right with moveinright

    rei "Doctor Eirin, I think they’re awakening!"

    e "Very good, reisen"

    pov "I got a boo boo"

    e "You have multiple bone fractures and severe radiation poisoning."

    pov "I want lollipop now"

    hide eirinNormal

    show eirinClosed at right

    e   "You will die in minutes without treatment."

    pov "I want green apple flavor plz."

    e "Reisen, Get the ingredients for the medicine"
    
    rei "Yes, Dr. Eirin"

    hide reisenConcerned with moveoutleft

    show eirinClosed at center with move

    show eirinNormal at center

    hide eirinClosed

    "Offscreen, Mokou" "Kaguya, it’s been 17000 years."

    "Offscreen, Mokou" "You still owe me 16$ dollars"

    rei "uh oh"

    hide eirinNormal

    show eirinConfused at center

    e "Oh no those two are fighting again."
    
    e "It looks like we’ll be waiting a while."

    e "Forgive me for not introducing myself, I am Eirin, the doctor of this clinic."

    e "{cps=1.5}...{/cps}"

    pov "({i}Quick i have to make small talk{/i})" 
    
    pov "So uh did you know three out of four people make up 75\% of the population?"
    
    pov "Crazy right?"

    hide eirinConfused

    show eirinClosed

    e "How did a human like you get so far in Gensokyo?"

    pov "Plot armor but i like to think its my charm and wit"

    e "Right." 

    pov "Yo is that the american flag back there"

    hide eirinClosed
    
    show eirinConfused

    e "Hm?"

    pov "America. the nation. the flag."

    hide eirinConfused

    show eirinNormal

    e "Oh, you must mean the moon invaders."
    
    pov "Of course something batshit crazy every single minute"

    pov "You’re gonna pull some wizardry bullshit in the next 2 minutes I can tell"

    hide eirinNormal

    show eirinConfused
    
    e "Wizardry? Well..."

    e "Have you ever heard of the curse of Apollo 13?"

    pov "what"
    
    pov "Wait so YOU MFS CAUSED APOLLO 13!?"
    
    e "No that’s"  
    
    e "Well..."
    
    e "Those were actions of the lunar capital."

    pov "What the fuck is a lunar capital?"
    
    "{i}Some explaining later...{/i}"

    hide eirinConfused
    show eirinNormal

    pov "Wow I knew the government was lying to me but the last thing I would expect to be the truth was that there are bunnies hidden on the moon attacking anyone who enters like it’s north Sentinel Island"
    
    e "Then perhaps your government covering up such dangerous knowledge is beneficial for humanity?"

    pov "That doesn’t matter cause I’m stuck in this little Alice in the Wonderland situation except its real and I now have radiation poisoning"
    
    hide eirinNormal
    show eirinClosed

    e "It seems you have been living past your lifespan."
 
    pov "Look who’s talking ms. Millennium you give the queen of England a run for her money wooo gottem"

    e "My potion is done."
    
    e  "All its missing are the pop tarts."

    e "Reisen will be here shortly with the last ingredients."

    e "Here's the medicine."
    
    pov "I don’t trust like that"
    
    e "Like i said without treatment you’ll die soon, so it’s in your best interest to take it."
    
    pov "Taste like watermelon seed"

    e "Here's an idea"

    e "Reisen, please escort [povname] to the border"

    rei "Alright when do i get my paycheck—"

    e "From there, you can escape to a nearby city"
    
    e "Good luck"

    show black
    with fade

    scene bg cafe tv
    with fade2

    pov "Hell yeah i made it out of that weird ass place now to go back home! I’m getting a flight back home—"

    $ renpy.movie_cutscene("go news.mkv", delay=None, loops=0, stop_music=True)
   
    show bg cafe tv
    with fade2

    pov "Ok so who tf told the un security council i have 74 nuclear warheads"
    
    show yukariNormal:
        alpha 0.0 xalign 0.5 yalign 1.0
        linear 2 alpha 1.0 xalign 0.5

    pause 2.0

    y "Hey"

    pov "NOT THIS BITCH AGAIN"

    y "I’ve just informed the FBI of your exact coordinates."

    pov "BRO WHAT THE FUCK"

    y "I also told the un security council you have 74 nuclear warheads in your possession"

    pov "AWWWWWW DAMNNNNNN IT WAS YOU"

    y "Not to worry war criminal, i brought you an escape! this portal back into gensokyo!"

    window hide

    pause 2

    window show

    pov "So do i take my chances back in that wonderland realm or do i partake in the famed don't drop soap challenge for the rest of my life idk i watched all of those larry lawton videos i think id be fine?"

    y "I'm shoving you inthat goddamn portal"

    show black
    with fade

    y "If you want to stop Kakkoi heres her casino"

    pov "Wow ok way to move the plot forward"

    "COMPUTER" "PLEASE ENTER PASSWORD"

    pov "Password…"

    pov "what anyone would have as their password!"
    
    pov "chupachupslover445"
    
    "COMPUTER" "ACCESS ACCEPTED"

    scene bg casino
    with fade2

    play music "<loop 0>audio/kakkoi.mp3" fadein 2.0

    show okuuNormal at left with moveinright

    show kakkoiNormal at farright with moveinright

    k "My money laundering and cloth drying scheme is working!"

    k "I AM INVINCIBLE! No one can fuck with Kakkoi!"

    k "I’ll have to give myself a promotion!"

    hide okuuNormal

    show okuuHappy at left

    o "When the world is money im going to buy a hazmat suit"

    k "You have as much taste as a carton of milk expired in 2005"
    
    k "Haha took me years to think of that"

    pov "years wasted"

    hide kakkoiNormal

    show kakkoiUnhappy at farright

    k "Wow."

    k "The caucacity of this mf."
    
    k "how the hell did you survive"

    hide kakkoiUnhappy

    show kakkoiSmoking at farright

    k "Doesn't matter"

    hide kakkoiSmoking

    show kakkoiPointing at farright
    
    k "We’re gonna fight now and beat your punk ass"

    pov "How is turning the entire planet into money beneficial for you?"

    hide kakkoiPointing

    show kakkoiSmoking at farright

    k "You’re asking the wrong questions, [povname]."

    k "It’s not about the money..."

    hide kakkoiSmoking

    show kakkoiUnhappy at farright

    k "Actually it is about the money."

    k "Sorry for the confusion"

    pov "go go gadget armed robbery"

    k "Oh yeah?"

    hide kakkoiUnhappy

    show kakkoiPointing at farright

    k "Come and get it"

    o "Yeah if you don’t come and get it, we’re gonna keep it! then you’ll be sorry!"
    
    k "lemme throws some money at them"
    
    k "Wait Okuu why does my bank account have -4x2^2 ฿ wtf did you do?"

    o "I bought two lifetime supplies of limes! For you and me!"

    window hide 

    pause 2.5

    window show 

    k "You know you’re the reason shampoo has instructions."

    hide okuuHappy

    show okuuConfused at left

    o "I like the taste"

    hide kakkoiPointing

    show kakkoiUnhappy at farright
    
    k "Well it looks like we failed lets go home"
    
    hide okuuConfused

    show okuuNormal at left

    o "So Kakkoi what are we gonna do tomorrow night?"

    hide kakkoiUnhappy

    show kakkoiSmoking at farright

    k "The same thing we do every night Okuu"

    k "Eat animal crackers until we pass out."

    hide okuuNormal with moveoutleft
    
    stop music fadeout 1.5

    play music "<loop 0.0>audio/main-menu-theme.mp3" fadein 2.0

    hide kakkoiSmoking with moveoutleft
    
    show reimuHappy at left with moveinright

    show marisaHappy at right with moveinright

    rei "You did it!"

    rei "That was very impressive!"

    show yukariNormal:
        alpha 0.0 xalign 0.5 yalign 1.0
        linear 2 alpha 1.0 xalign 0.5

    hide reimuHappy   with moveoutleft

    hide marisaHappy  with moveoutright

    

    pov "do i get to leave now and go back home?"
    
    y "No youre still stuck here."
    
    pov "wtf"

    stop music fadeout 5

    show black
    with fade3

    $ renpy.movie_cutscene("credits v2.mkv", delay=None, loops=0, stop_music=True)

    # This ends the game.

    # "Thank you to Big Boo, gatomon20xx, nekon, stat, and Kdzki for their art design."
    # "Thank you to Domomess for the logo and thumbnail design."
    # "Thank you to Eggnnog and mikemburgia for acting roles. "
    # "Thank you to Kenji for game programming."
    # "Thank you to Kronington for leading, script writing, video production, and music."


    return

    # Programmed with ❤️ by Kenji