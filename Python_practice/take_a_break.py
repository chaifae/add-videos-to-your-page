import webbrowser
import time


breaks = 0

print "This program started on " + time.ctime()

while breaks < 3:
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=OPf0YbXqDm0")
    breaks += 1
