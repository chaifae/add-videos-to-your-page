import webbrowser

name = raw_input("What is your name?   ")

print "Hello " + name + "!"
whatdo = raw_input("What would you like to do today?   ")

if "movie" in whatdo:
    print "OK, lets watch a movie together!"
    webbrowser.open("http://movies.disney.com/all-movies")
elif "read" in whatdo:
    print "Alright, lets find a book to read!"
    webbrowser.open("http://www.readanybook.com/")
elif "game" in whatdo:
    print "I'd love to play a game with you!"
    webbrowser.open("http://www.addictinggames.com/")
elif "learn" in whatdo:
    print "I'll teach you something new!"
    webbrowser.open("https://www.udacity.com/")
else:
    print "I don't feel like doing that today."
    print "Why don't you go outside?"
    print "I'll take a nap and be here when you get back!"
    print ""
    print "Goodbye!"
