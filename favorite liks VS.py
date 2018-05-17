import pyautogui as pg
import webbrowser

videos = ["https://www.youtube.com/watch?v=iRXJXaLV0n4"]

music = ["https://www.spotify.com/us/"]

answer = pg.prompt(
"""
a) watch videos
b) listen to music

"""
    )

if answer == "a":
    for i in videos:
        webbrowser.open(i)
elif answer ==  "b":
    for I in music:
        webbrowser.open(i)
