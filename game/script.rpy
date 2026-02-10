# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Colette", color = "#E10072")
define a = Character("Anya", color = "#FF5400")
define m = Character("Miles", color = "#66FF00")

transform smallright:
    zoom 0.7
    xalign 2.0
    yalign 1.0

transform smallleft:
    zoom 0.7
    xalign -0.8
    yalign 1.0

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
    play music "happy-background-music-442792.mp3"
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
    pause 6.5
    scene near 
    with fade

    return
