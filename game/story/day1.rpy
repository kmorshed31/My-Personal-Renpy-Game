    
label day1:
    # scene 1
    scene bg bedroom
    "..."
    "..."
    "..."
    a angry "Jorj, wake up! For heaven's sake!" with hpunch
    me neutral "..."
    "Suddenly, he felt a hard slap on the legs."
    me neutral "Aaagh!"
    a angry "Get up! I will not let you sleep anymore! Now!" with hpunch
    me sad "Huhhh..."   
    a angry "Now! Get up! "
    "She slaps his legs again. This time, harder."
    me neutral "Stop! I'm up. I'm up. I'm up!" 
    a neutral "Go brush your teeth and take a bath."
    "With a groan, Jorj gets up from the bed. He then rubbed his eyes and sighed. However he did not get up."
    a angry "What are you waiting for? Go!"
    "He then gets up and walks to the bathroom slowly with blurry eyes while picking eye crust."
    #scene 2
    scene bg bathroom with fade
    pause 2.0
    "He picks up the brush from the sink, puts tooth paste on it and after putting his trousers down sits on the toilet to take a dump."
    me neutral "{i}Damn... I am constipated. I have to get some laxatives tonight.{/i}"
    pause 2.0
    "After he finishes his business, he rinses his mouth and face, then takes a quick shower."
    me neutral "{i}Aah, I have Mr. Hollen's class today... That son of a bitch makes me want to kick his face and make him drink sewage water.{/i}"
    "He finishes his bath and then goes to the dining room. His father is reading a newspaper."
    "Both his parents come up to him and sit in front of him as if they wanted to announce or tell something important to him."
    me neutral "{i}I wonder what they want to talk about...{/i}"
    #fade
    scene bg dining_room with fade
    pause 2.0
    a neutral "Jorj, we need to tell you something. We went to the doctor yesterday. And there is good news."
    me neutral "What is it?"
    m neutral "You are becoming a big brother."
    me neutral "..."
    menu:
        "Express joy":
            $ dad_relationship += 1
            $ mom_relationship += 1
            me happy "Wow, so we are going to have a baby in the house!"
            m happy "Yes, and your grandma is going to stay with us for 9 months till your mother gives birth, to take care of her. And you must help out too!"
            me happy "Yes, wow it feels weird. There is going to be someone younger than me in this house. But I am happy."
            a happy "We are also very happy, Jorj."
            m happy "You must do your homework properly and help your mother out."
            "Annah then warmly hugs Jorj."
            me "I will do that, Dad."
        "Express concern":
            $ intelligence += 0.1
            me neutral "But isn't mom a bit too old to be having a baby? Mikhaeela is already 16. I am 13."
            m happy "It seems our son is quite smart to be worrying about such things."
            a happy "Well, it's not uncommon for women to have children later in life. And I really wanted a baby. I miss the time when you were a baby."
            m neutral "I also wanted a baby. I thought you would learn to be more responsible if you had a younger brother or sister."
            me neutral "Okay...:"
            a happy "Hey... my little son is more worried about my age than I am..."
    me neutral "Does Mikhaeela know about this?"
    a neutral "Not yet. She has not woken up yet. Her classes start at 11. We will tell her when she's up."        
    a happy "Anyway, you have to hurry up."
    me "Sure!"
    me neutral "{i}I will take my time to finish eating...{/i}"
    "While eating breakfast, Jorj eats slowly, peeking and reading the newspaper his father is reading over his shoulder."
    "Mikhaeela goes to the bathroom, still in her pajamas."
    a neutral "She's woken up."
    "After a while, Mikhaeela comes to the dining room, still in her pajamas. She comes to the table, sits down with legs folded and starts eating."
    a neutral "You're awake."
    mi neutral "Hmm... I had to pee. And my drowsiness went away after that."
    m neutral "There is a good news, Mikhaeela."
    mi neutral "What is it?"
    m neutral "Your mother is pregnant. You are going to have a little brother or sister."
    "Mikhaeela stops eating for a moment, then looks at her parents."
    "..."
    mi neutral "Are you serious?"
    "Annah nods yes, smiling."
    "Mikhaeela jumps from her seat, hugs her mother tightly and starts giggling."
    mi happy "Congratulations, mom! I am so happy! I am going to be a big sister... again." with vpunch
    mi neutral "But... aren't you a bit too old to be having a baby? You are already 32."
    a neutral "Well, I really wanted another baby. And your father also wanted one."
    m neutral "Yes, we both wanted another child. And it's not uncommon for women to have children later in life."
    mi neutral "I see... Well, I am happy for you both!"
    m neutral "You know what this means, right? You have to help your mother out more. Pracically do everything she does as time progresses during the next 9 months."
    mi neutral "Sure, dad. I will do that."
    me neutral "{i}Hmm... I wonder how having a baby in the house will change things...{/i}"
    "After finishing breakfast, Jorj goes to his room to get ready for school."
    scene bg bedroom with fade
    pause 2.0
    "He changes into his school uniform, packs his bag and puts on his shoes."
    "He glanced at his ball lying on the floor. After coming back from school, he will go outside to play."
    "Increasing immigration. He was reading his father's newspaper."
    me neutral "{i}Ersenia has record migration hike. Half a million people from Tameirah. The total population is a hundred million already plus piling up the Tameiris.{/i}"
    me neutral "{i}The government should do something about this. Crime is too high. All these fucking Tameiris steal and rob. These deplorables have made my neighborhood less safe than just a few years ago.{/i}"