# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Colette", color = "#E10072")
define a = Character("Anya", color = "#FF5400")
define m = Character("Miles", color = "#66FF00")
define s = Character("Sweetheart", color = "#FFA0F9")

transform smallright:
    zoom 0.7
    xalign 2.0
    yalign 1.0

transform smallleft:
    zoom 0.7
    xalign -0.8
    yalign 1.0

transform bigleft:
    zoom 4.7
    xalign -0.34
    yalign -1.7

transform extrasmallright:
    zoom 0.3
    xalign 1.0
    yalign 1.0

label scene_loop:
    $ i = 0
    while i < 6:
        scene sleep
        pause 0.25
        scene open 
        pause 0.25
        $ i += 1
    return

# The game starts here.

label start:
    play music "snoring-71560.mp3" fadein 1.0
    scene sleep
    with fade
    pause 7.5
    stop music
    play music "happy-background-music-442792.mp3" fadein 0.5
    call scene_loop
    scene yawn
    play sound "yawning-6096.mp3" volume 8.0
    pause 2.5
    show colette glad 
    play sound "aw-86103.mp3" volume 3.5
    c "Aw... It's 💝 Valentine's Day 💕 today!"
    show colette confident 
    c "I'm so excited! It'll be such a lovely day!"
    scene bu
    play sound "sad.mp3" volume 10.5
    c "I mean... I don't have a boyfriend... yet..."
    show colette yes
    c "But my bestie Anya is going to hang out with her boy today."
    c "She wants me to go with them."
    show colette confident
    play sound "chuckle.mp3" volume 2.5
    c "It'll be so fun! Trust!"
    show colette glad
    c "Off to Anya's!"
    c "Let's go!!! 💞"
    scene house
    with fade
    play music "footsteps-dirt-gravel-6823.mp3" volume 4.5
    pause 4.5
    scene near 
    with fade
    pause 2.5
    stop music
    scene room 
    with fade
    play sound "opening-door-411632.mp3" volume 2.5
    play music "golden-sun-318286.mp3" fadein 1.0
    show colette glad at smallleft
    with moveinright
    play sound "hello-278029.mp3" volume 3.5
    c "Hello!"
    show anya normal at smallright
    with moveinleft
    play sound "why-hello-there-103596.mp3" volume 3.5
    a "Why hello there!"
    show colette yes at smallleft
    with dissolve
    c "So bestie, has you boyfriend arrived yet?"
    show anya smile at smallright
    with dissolve
    c "Well, yeah! He's a super punctual guy!"
    show colette glad at smallleft
    with dissolve
    play sound "chuckle.mp3" volume 2.5
    c "Haha! I bet he's only on time for {i}you{/i} -- can't bear to make you wait!"
    show colette believe at smallleft
    with dissolve
    c "Anyway... where is he now?"
    show anya normal at smallright
    with dissolve
    a "Well... he's cooking for us, but with his cooking skills..."
    show anya hap at smallright
    with dissolve
    a "Let's hope he doesn't poison us on Valentine's Day lol!"
    show colette glad at smallleft
    with dissolve
    show anya smile at smallright
    with dissolve
    a "Anyway, come wait in my room! We can make some valentine cards 💌!"
    stop music fadeout 1.0
    scene min
    with fade
    play sound "later.mp3" volume 3.5
    pause 5.0
    scene inside 
    with blinds
    show smoke 
    with dissolve
    play music "fire.mp3" fadein 3.0
    show colette scared at smallleft
    with moveinright
    play sound "girl-oh-no-150550.mp3" volume 2.5
    c "Oh no! There's a lot of smoke! 💨 We have to leave quickly! 🔥"
    hide colette scared
    with moveoutleft
    show more
    with dissolve
    pause 3.0
    stop music fadeout 0.8
    play sound "magic-03-278824.mp3"
    scene pink 
    with Fade(0.0, 0.0, 0.35)
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    pause 2.0
    show miles embarrassed at extrasmallright
    with moveinright
    m "Ummm... sorry girls. My bad..."
    show colette believe at smallleft
    with moveinright
    c "Wait. What is this super pink and magical place that pulls at your heartstrings and gets you so whipped on love?!"
    hide colette believe
    with dissolve
    show sweetheart at bigleft
    with dissolve
    s "This is the {b}Love Kingdom{/b}!"
    m "Ok? Sorry, but, who... no, what are you?"
    s "Oh, my honored guests, I'm your guide here in the Love Kingdom! You guys can call me Sweetheart!"
    m "Sweetheart?!"
    hide miles embarrassed
    with dissolve
    show colette believe at smallright
    with dissolve
    c "Well, she {i}is{/i} literally a heart..."
    s "My distinguished guests, let me give you a tour of our kingdom!"
    c "What kingdom? I just see nothig but pink everywhere!"
    c "Oh! That's because we haven't offically entered the mingdom yet."
    c "The Love Kingdom is divided into seven villages -- {i}Eros{/i}, {i}Philia{/i}, {i}Storge{/i}, {i}Agape{/i}, {i}Ludus{/i}, {i}Pragma{/i}, and {i}Philautia{/i}."
    hide colette believe 
    with dissolve
    show anya normal at smallright
    with dissolve
    a "Oh! Those are the {i}Seven Classical Loves{/i}!"
    s "Yes, clever girl! The seven loves represent a modern integrative framework rooted in ancient Greek philosophy."
    s "It is designed to capture the full spectrum of the human affection."
    s "This taxonomy distinguishes seven distinct qualities if attachment, each with its own psychological structure, ethical demands, and social function."
    s "The seven loves thus constitute a moral psychology of attachment -- a map for navigating human connection with intentionality and ethical awareness."
    hide anya normal
    with dissolve
    show colette believe at smallright
    with dissolve
    c "Ok... which one are we going to visit first?"

    return
