# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Colette", color = "#E10072")
define a = Character("Anya", color = "#FF5400")
define m = Character("Miles", color = "#66FF00")
define s = Character("Sweetheart", color = "#FFA0F9")

transform smallright:
    zoom 0.7
    xalign 1.6
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
    s "Oh! That's because we haven't offically entered the mingdom yet."
    s "The Love Kingdom is divided into seven villages -- {i}Eros{/i}, {i}Philia{/i}, {i}Storge{/i}, {i}Agape{/i}, {i}Ludus{/i}, {i}Pragma{/i}, and {i}Philautia{/i}."
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
    show anya smile at smallright 
    with dissolve
    a "Ahem... since it's Valentine's Day today, and Miles is here with me, can we go visit {i}Eros{/i} first... We can go visit {i}Philia{/i} right after... sorry, Colette..."
    show colette glad at smallright
    with dissolve
    c "Oh, no worries, girl!"
    show colette yes at smallright
    with dissolve
    c "I don't understand any of those seven types of love anyway, so..."
    s "Great choices! We will be heading to {i}Eros{/i} now!"
    play sound "magic-03-278824.mp3"
    scene eros
    with Fade(0.0, 0.0, 0.35)
    play music "nastelbom-romantic-436840.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "Welcome to {i}Eros{/i}!"
    show miles heart at extrasmallright
    with dissolve
    m "Gosh! This is such a sweet place! I can feel my sex drive kicking in. All those love hormones, hitting my brain instantly."
    hide miles heart 
    with dissolve
    show anya hap at smallright
    with dissolve
    a "Yeah! This is the most intense kind of love lol!"
    a "{i}Eros{/i} is the love of passion and desire."
    s "Right! It's named after the Greek god of love!"
    s "This is romantic, physical love. This is the spark,the chemistry, the butterflies."
    show anya smile at smallright
    with dissolve
    a "Yeah... It's the kind of love that pulls you towards someone -- body and soul."
    show anya normal at smallright
    with fade
    s "But be careful, while {i}Eros{/i} is thrilling, it can fade quickly if it's not rooted in something deeper..."
    show miles normal at extrasmallright
    m "Oh don't you worry, my love towards Anya {b}is{/b} rooted deeply, right? 😘"
    hide miles normal
    show anya smile at smallright
    with dissolve
    a "🫶🏻 We'll see..."
    show anya normal at smallright
    with dissolve
    a "But anyway, we should go to {i}Philia{/i} right now, I promised Colette we'd go there."
    s "Okay people, let's go!"
    play sound "magic-03-278824.mp3"
    scene philia
    with Fade(0.0, 0.0, 0.35)
    play music "friends.mp3" fadein 1.5
    play sound "virtual_vibes-children-giggling-kids-laughing-hd-378111.mp3"
    show sweetheart at bigleft
    with dissolve
    s "We're here! This is {i}Philia{/i}!"
    show colette confident at smallright
    with dissolve
    c "Hehe, this place obviously has something to do with friendship 💗, right?"
    s "Yes. {i}Philia{/i} is the love of friendship. Honest, loyal, and deeply supportive."
    s "It's the bond between close friends, teammates, or even siblings!"
    show colette glad at smallright
    with dissolve
    c "I know, this love is based on trust, respect, and shared values."
    hide colette 
    with dissolve
    show anya smile at smallright
    with dissolve
    a "It is the kind of love where words aren't always needed."
    s "Correct! {i}Philia{/i} is usually steady and long-lasting."
    a "It's a love that says, \"I've got your back\"."
    play sound "magic-03-278824.mp3"
    scene storge
    with Fade(0.0, 0.0, 0.35)
    play music "family.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "So, this one is my fav!"
    s "Welcome to {i}Storge{/i}!"
    show colette confident at smallright
    with dissolve
    c "I can tell you really love here! You didn't even give us a heads-up and just brought us here."
    show colette yes at smallright
    with dissolve
    c "Alright then, the stage is all yours. Tell us more about this place!"
    s "{i}Storge{/i} is the gentle protective love found within families."
    hide colette yes
    with dissolve
    show anya normal at smallright
    with dissolve
    a "Oh, is it the love parents feel for their children or siblings feel for each other over time?"
    s "You got two for two! Nice, both are correct! {i}Storge{/i} grows naturally, you don't have to earn it, it's just there!"
    s "This is why I love it so much -- {i}Storge{/i} is quiet but powerful -- a love that holds that even through life's ups and downs!"
    hide anya normal 
    with dissolve
    show miles pleasant at extrasmallright
    with dissolve
    m "Cool! That sounds super sweet! 🏡"
    show miles embarrassed at extrasmallright
    with dissolve
    m "But... we've already talked about romantic love, deep friendship, and familial love. What other kinds are even left?"
    s "Haha, I'll show you!"
    play sound "magic-03-278824.mp3"
    scene agape
    with Fade(0.0, 0.0, 0.35)
    play music "abydos_music-the-holly-and-the-ivy-195003.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "This is {i}Agape{/i}! {i}Agape{/i} is the highest, most spiritual form of love!"
    show anya normal at smallright
    with dissolve
    a "I can feel it's unconditional, sacrificial, and selfless..."
    s "Right. It's the love that gives without expecting anything in return."
    s "{i}Agape{/i} is found in acts of kindness, compassion for strangers, or loving someone even when it's hard."
    show anya smile at smallright
    with dissolve
    s "Ah! It's the kind of love the world needs more of!"
    play sound "magic-03-278824.mp3"
    scene ludus
    with Fade(0.0, 0.0, 0.35)
    play music "geoffharvey-playful-mr-jelly-rolls-392651.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "Now, this is {i}Ludus{/i}. 😉 {i}Ludus{/i} is the love of flirtation, teasing, and light-hearted connection."
    s "It's the butterflies of early romance. 💘"
    show miles normal at extrasmallright
    with dissolve
    m "Ha, I know all about it! The playfulness in texting late at night, the fun of just being silly together... {i}Ludus{/i} doesn't take itself too seriously. It's love with a wink and a laugh!"
    s "But too much {i}Ludus{/i} without commitment can feel shallow over time."
    show miles embarrassed at extrasmallright
    with dissolve
    m "That's true. Anyway, where are we going left? I'm actually quite excited now! There are only two more left, right?"
    s "Yes. And what about... I let you guys choose?"
    menu:
        "{i}Pragma{/i}":
            jump first
        "{i}Philautia{/i}":
            jump second
    
label first:
    play sound "magic-03-278824.mp3"
    scene pragma
    with Fade(0.0, 0.0, 0.35)
    play music "old.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "{i}Pragma{/i} is the love that grows with time, effort, and understanding."
    show colette confident at smallright
    with dissolve
    c "You know what, I studies that in school! It's found in long-term relationships, mature marriages, and deep partnerships."
    s "Absolutely! {i}Pragma{/i} is built, not found."
    s "It's about choosing love, even when it's not exciting."
    s "This love is strong because it's rooted in patience, compromise, and shared life goals."
    play sound "magic-03-278824.mp3"
    scene philautia
    with Fade(0.0, 0.0, 0.35)
    play music "calm-jazz-220610.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "Here is the last stop of your tour -- {i}Philautia{/i}."
    s "Before you can truly love others, you have to love yourself."
    show anya normal at smallright
    with dissolve
    a "So... {i}Philautia{/i} is self-love!"
    hide anya normal
    with dissolve
    show colette believe at smallright
    with dissolve
    c "But not the selfish kind..."
    show colette yes at smallright
    with dissolve
    c "The healthy kind!"
    s "Yeah! It's accepting yourself, caring for your body, setting boundaries, and believing you are worthy of love."
    show colette confident at smallright
    with dissolve
    c "{i}Philautia{/i} reminds us that we matter too!"
    jump end
    
label second:    
    play sound "magic-03-278824.mp3"
    scene philautia
    with Fade(0.0, 0.0, 0.35)
    play music "calm-jazz-220610.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "Here is -- {i}Philautia{/i}."
    s "Before you can truly love others, you have to love yourself."
    show anya normal at smallright
    with dissolve
    a "So... {i}Philautia{/i} is self-love!"
    hide anya normal
    with dissolve
    show colette believe at smallright
    with dissolve
    c "But not the selfish kind..."
    show colette yes at smallright
    with dissolve
    c "The healthy kind!"
    s "Yeah! It's accepting yourself, caring for your body, setting boundaries, and believing you are worthy of love."
    show colette confident at smallright
    with dissolve
    c "{i}Philautia{/i} reminds us that we matter too!"
    play sound "magic-03-278824.mp3"
    scene pragma
    with Fade(0.0, 0.0, 0.35)
    play music "old.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "At last, {i}Pragma{/i} is the love that grows with time, effort, and understanding."
    show colette confident at smallright
    with dissolve
    c "You know what, I studies that in school! It's found in long-term relationships, mature marriages, and deep partnerships."
    s "Absolutely! {i}Pragma{/i} is built, not found."
    s "It's about choosing love, even when it's not exciting."
    s "This love is strong because it's rooted in patience, compromise, and shared life goals."


label end:
    play sound "magic-03-278824.mp3"
    scene pink
    with Fade(0.0, 0.0, 0.35)
    play music "sweet-acoustic-guitar-music-311691.mp3" fadein 1.5
    show sweetheart at bigleft
    with dissolve
    s "So, thank you guys for visiting our Love Kingdom."
    s "I hope you learnt something new, and..."
    s "❤️ Happy Valentine's Day! 💗"



    return
