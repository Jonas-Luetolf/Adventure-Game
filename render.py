#importieren von time,os und sys
import time
import os
import sys


class render:

    #Konstruktor
    def __init__(self):

        #erstellen von colors dictionaty
        self.colors={"green":'\033[92m',
                        "orange":'\033[93m',
                        "red":'\033[91m',
                        "white":'\033[0m'}
    
    
    #clear Methode
    def clear(self):

        #für Windows
        if os.name=="nt":
             os.system("cls")

        #für Linux und MacOs
        else:
             os.system("clear")
           

    #print Methode
    def print(self,text,color="white"):

        #zusammensetzen von Text und Farbcodes
        text=(self.colors[color]+text+self.colors["white"]+"\n").replace("/oe","ö").replace("/ae","ä").replace("/ue","ü")
        
        #ausgeben von Text 
        for char in text:
            #leeren des Buffers
            sys.stdout.flush()

            #printen eines chars
            sys.stdout.write(char)
            
            #0.015s warten
            time.sleep(0.015)


    #input Methode
    def input(self):
        return (input().replace("ö","/oe").replace("ä","/ae").replace("ü","/ue"))

