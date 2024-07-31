# how to install predefined module
from gtts import gTTs
from os import system
# text=input("Enter your message : ")
txt="my name is shubham"
output=gTTs(text=txt,lang="hi")
output.save("pit.mp3")
system("pit.mp3")