import webbrowser
name = "vaughn"

subjects = ["english","spanish","history","math","science"]

print ( "hello " + name)

print (subjects) 

for i in subjects:
    print ( "one of my classes is " + i)

characters = ["Nicky", "Ricky", "Dicky", "Dawn"]

for i in characters:
    if i == "Nicky":
       print (i + " is the best character.")
    elif i == "Dicky":
        print (i + " is the worst character.")
    elif i == "Dawn":
        print (i + "is the only girl out of the four.")
    else:
        print ("one of the best characters is " + i)

movies = []

while True:
    print("what is a movie you like? type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("one of your favorites is " + i)
    webbrowser.open(i)
