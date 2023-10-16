print("WELCOME TO MORGATH'S TOWER OF CHAOS an adventure game by Douglas Rohal.\n This is a beta version of an adventure book I wrote in 2017")
print('')
print("You are Stub, a rather unimpressive Wizard's Apprentice with a rather unimpressive name. \nYou took the weekend off to party in the near by village and woke up with a hangover in a ditch.\n Pointed Wizard Hat on your head you brush of the dirt from your robe and climb the hill to your Wizard Master Morgath the Mysterious to start the week's grind all over again. ")
door_action=input("\nYou reach the front door to the tall and not at all run down looking tower. The door is made of a solid oak and has gold inlays and writing,\n but you never learned elfish or whatever it was, you tug on the large iron door handel but it seams to be locked. Your mentor has not yet given you a key.\n Do you GO AROUND BACK, LOOK IN THE ROCK GARDEN, or FORCE THE DOOR OPEN :")
if door_action.lower()=='go around back':
    print('\nYou walk across the rock garden and go around to the back of the tower ready to open up that patio door that allways is unlocked but instead come face to face with the towers gaurd dog, a twelve foot tall Dog, and oh no he looks like he has not eaten recently. Your pointy hat cant save you now. You have died.')
if door_action.lower()=='force the door open':    
    force_door_cons=input('\nYou take a few steps back, you were never a line backer or anything in sports, kids were cruel, but your willing to put your shoulder into the door if it means you can keep your internship. \n You rush the door and bounce of much like a beachball, with the same effect. The door gloes an ominous red.')
    print('\nYou rub you sore shoulder and re-adjust your hat, roll up the sleeves of your robes, take a few steps backs and try again.\n You ram the door yet again with your shoulder. You would feel the joint problems if the doors omminious red, didnt fill your vision and then turn you into dust,leaving your ashen remains for the maid that comes around once a week to clean up.')

#correct path door entry
if door_action.lower()=='look in the rock garden':
    key_find=input("\nIn the rock garden is a rather fetching statue of a toad and a frog. You have to know at a glace which is which because it takes 10X the magical energy to turn somone into a toad.\n It is wizarding 101!.\n Either way the Stone frog has a dull green orb on its back, and the stone toad has a bright red stone on its back. Do you wish to EXAMINE THE FROG, or EXAMINE THE TOAD : ")
    if key_find.lower()=='examine the toad':
        print("You examine the toad even though all your wizardly instincts tell you to avoid it at all cost, you grab it by the red gem and suddenly your vision is filled with blinding light. You have been turned into a stone statue of yourself. Unmoving and better at small talk than ever.\nYou have died.")
        quit

    if key_find.lower()=='examine the frog':
        print('\nYou lift up the frog, and are surprise by its light weight, and smooth textures. This is not a stone frog at all you realised. Its plastic! Your mentor was a cheap skate alright. Then again you should have known as you are an unpaid intern. \nYou toss the frog back into the rock garden and as it lands you hear a poping sound and the clanking of metal.\n you look down to find a hatch on the bottem of the frog now open and a key next to it on the ground.\n You pick up the key and make your way back to the door to unlock it. ')
        print('\nYou arive in the entry hall of Morgaths tower. It is dark and smells of sulfure, it was not like this the last time you were around.\n The very fancy rug you noramly see on the floor is rolled up in the corner and a circle of chaulk with mystical runes is in its place. A note lays on the ground. It is writen by your Mentor! "If I am not back from other dimmention by monday recast spell, Help." ')
        print(' \nOh no! Morgath seems to be trapped himself in another dimmention while you were gone! If only he flowed wizard OSHA guidelines and did not make on otherworldy portal with out a certifate and a general contracter on hand.')
        dirrection_first_floor_choice=input('\n Well it looks like its up to you to save him from his own problems, after all your his intern. There are four dirrections you can go to start your quest UP THE STAIRS which you are pretty shure Morgath did on the weekend without a permit considering how much they move when you walk up them.\n You could go to your left INTO THE LOUNGE and look for clues,\n You can go TO THE RIGHT where you have never been allowed to go before, or TURN AROUND AND LEAVE out the door you came. ')
        if dirrection_first_floor_choice.lower()=='turn around and leave':
            print(' You turn around and leave the tower through the door you just opened. You do not get paid enough to risk your hide to save a rather abusive and fiddly employer. In foract you do not get paid at all. So he can rot in whatever dimention he lost himself in.')
        if dirrection_first_floor_choice=='TO THE RIGHT':
                dinning_room=input(' You reach for the door handel, surprise to find it unlocked, you make your way into what is apperently the dining room.\n You look around and find that the table is fully catered and covered in food, including a full sized roasted Pig. There is also a patio door and somthing moving in the back garden. Do you SIT DOWN AND EAT SOME FOOD? or GO TO THE BACK GARDEN?')
                if dinning_room=='SIT DOWN AND EAT SOME FOOD':
                        print(' You fill up a plate with all the food you can muster and sit down at a chair, the chair is oddly sticky, but that has never stoped you before. Unknowingly as you eat your food the chair keeps getting lower and lower for some reason. It turns out that the chair is not at all but a mimic that looks like a chair! You are eaten by the mimic chair. You have died.')
                if dinning_room=='GO TO THE BACK GARDEN':
                        print(' You open up the patio door and check out the back yard, to find a gaurd dog with three heads. He appernently was fed for the past couple days. You have died.')
        if dirrection_first_floor_choice.lower()=="into the lounge":
           print("You open the door to the lounge, a nice room with many books, Morgath the mysterious's rather confortable chair sits infront of a crackeling fireplace. ")
l_room_option=input("There is a small note under a glass of wine on the side table to Morgath's Chair which seems nicer by the minute, it reads Secret Entrances for dumbies volume 12. Do you want to CHECK THE BOOKCASE, or SIT DOWN AND ENJOY THE WINE? : ")
if l_room_option.lower=='SIT DOWN AND ENJOY THE WINE':
                print(' You sit down in the well apolsterd confortable chair in front of the crackleing fire place, it is down right relaxing. You take a sip from the wine glass and gaze into the fire. Hello? Stub? oh no, it seams Morgath was working on making himself immune to poison and you caught some of his last doses. You have died, serves you right for drinking even when you have a hangover. ') 
if l_room_option.lower=='CHECK THE BOOKCASE':
                    print('You move over to the very tall bookcase.')
bookcase_look=input('You look at the bookcase and look for a book. Wait what did that note say again? POST MORTEM COMUNICATIONS, HIDDEN TRAP ENTRANCES FOR THE INCOMPOTENT VOL 12, or SECRET ENTRACES FOR DUMBIES VOLUME 12? :')
if bookcase_look=='HIDDEN TRAP ENTRANCES FOR THE INCOMPOTENT VOL 12':
                     print('You pull out the book Hidden trap entrances for the incomptent vol:12, you hear a click and a panel falls out from under you revealing spikes, spining blades, and many many dogs with very sharp teeth, and well I would love to tell you what happend to your very fragile body, but this program needs to be in the rated T for Teens bin. So suffice it to say you died')
                     quit
if bookcase_look=='POST MORTEM COMUNICATIONS':
        print('You pick up the book labeld post mortem comunications. You flip to a random page and the book starts smoking, untill sudenly it exploads vaporising you instantly leaving only your hat behind. You have died.')
        quit
if bookcase_look=='SECRET ENTRACES FOR DUMBIES VOLUME 12':
        print('You attempt to pull out the book but it seams to be stuck on one of its corners you tug and tug. Untill you final give up, and wait. Was this bookshelf always facing the dirrection?\n No you walk around the moved bookshelf to find a stairway going down. You make your way down the stairs, and find yourself at the end of the program for now. ')