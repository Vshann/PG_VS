import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/user/yourteachermathhelp"]

music = ["https://www.youtube.com/watch?v=EvsXkwgMFGE"]

answer = pg.prompt(
"""
Which do you like more?
"""
    )

if answer == "a":
for i in videos:
        webbrowser.open(i)

elif answer == "b":
    for i in music:
        webbrowser.opem(i)
