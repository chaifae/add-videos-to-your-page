import urllib

def read_text(file_to_read):
    input_file = open(file_to_read)
    contents = input_file.read()
    input_file.close()
    speach_converter(contents)

def speach_converter(text_to_convert):
    connection = urllib.urlopen("http://isithackday.com/arrpi.php?text=" + text_to_convert)
    output = connection.read()
    print output
    connection.close()

def convert():
    print "This program will convert text to Pirate-speak."
    print "Are you inputting the text by using a file? Y/N"
    yn = raw_input(">> ")
    if "y" in yn:
        print "Please enter the file path exactly."
        path = raw_input(">> ")
        read_text(path)
    else:
        print "Type what you want to say, and I will convert it to Pirate-speak for you."
        typed_input = raw_input(">> ")
        speach_converter(typed_input)
        
    print "Try again? Y/N"
    yn = raw_input(">> ")
    if "y" in yn:
        convert()
    else:
        print "Goodbye."
    
convert()

