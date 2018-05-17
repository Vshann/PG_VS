import pyautogui as pg
import time
import webbrowser

points = 0



# question 1

answer = pg.prompt(
"""
which would you rather do?

a)eat worms
B)eat grass
c)eat wood

"""
)

# give points

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



# question 2

answer = pg.prompt(
"""
which would you rather watch?

a)watch the big bang theory
B)watch fuller house  
c)watch rick and morty

"""
)

# give points

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



# question 3

answer = pg.prompt(
"""
which would you rather eat?

a)eat chocolate ice cream
B)eat vanilla ice cream
c)eat strawberery ice cream 

"""
)

# give points

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3


# question 4

answer = pg.prompt(
"""
which would you rather play?

a)Fortnite 
B)COD
c)Gta (online)

"""
)

# give points

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



# end of survey

pg.alert("you are...")

#Kim Kardashian
if points < 5:
    pg.alert ("Kim Kardashian")
    webbrowser.open("https://www.youtube.com/watch?v=NWdc7PyZNLA")

#Kourtney kardashian
elif points >= 5 and points <10:
    pg.alert ("Kourtney Kardashian")
     webbrowser.open ("https://www.youtube.com/watch?v=_RZLzhD5k2k")

#Khloe Kardashian
elif points <=10 and points >15: 
    pg.alert ("Khloe Kardashian")
     webbrowser.open ("")

#Rob Kardashian
elif points <=15 and points >20:
    pg.alert ("Rob Kardashian")
     webbrowser.open ("")

