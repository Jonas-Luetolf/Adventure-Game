
import time
import os
import sys


class render:

    
    def __init__(self):

        #erstellen von colors dictionaty
        self.colors={"green":'\033[92m',
                        "orange":'\033[93m',
                        "red":'\033[91m',
                        "white":'\033[0m'}
    
    
    
    def clear(self):

        #für Windows
        if os.name=="nt":
             os.system("cls")

        #für Linux und MacOs
        else:
             os.system("clear")
           

    
    def print(self,text,color="white"):

        #zusammensetzen von Text und Farbcodes
        text=(self.colors[color]+text+self.colors["white"]+"\n").replace("/oe","ö").replace("/ae","ä").replace("/ue","ü")
        
        #ausgeben von Text 
        for char in text:
            #leeren des Buffers
            sys.stdout.flush()

            
            sys.stdout.write(char)
            
            
            time.sleep(0.015)


    
    def input(self):
        return (input().replace("ö","/oe").replace("ä","/ae").replace("ü","/ue"))

