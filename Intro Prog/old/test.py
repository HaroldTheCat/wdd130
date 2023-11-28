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