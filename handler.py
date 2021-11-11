#importieren von json und render
import json
import render as r


#handler Klasse
class handler:

    #Konstruktor
    def __init__(self,path):

        #öffnen von json
        with open(path,"r") as f:
            self.data=json.load(f)   

        #erstellen von render instanz
        self.render=r.render()

        #erstellen von Variabeln
        self.frame_data=""
        self.next_frame_data=""
        self.text_color=""
        self.text_data=""


    #print Frame Methode  
    def print_frame(self):
            #Konsole leeren
            self.render.clear()

            #text ausgeben
            self.render.print(self.text_data,self.text_color)


    def set_variables(self,index):
        #zuweisung von Variabeln
            self.frame_data=self.data[index]
            self.next_frame_data=self.frame_data["next"]
            self.text_data=self.frame_data["text"]
            self.text_color=self.frame_data["color"]
            


    #load_by_keywoard Methode
    def load_by_keyword(self,action):
        
        try:
            #laden von neuem frameindex
            
            index=self.next_frame_data[action]
            #überprüfen ob END
            if index=="END":
                return index
            
            #Variabeln neu setzen
            self.set_variables(index)

            #Text ausgeben
            self.print_frame()
            
            #True zurückgeben falls fehlerlos
            return True

            


        except:

            #printen von fehlertext
            self.render.print("Unbekannte Option",color="red")

            #False zurückgeben falls fehler aufgetreten sind
            return False


        
    

    #load_by index Methode
    def load_by_index(self,index):

        #setzen der Variabeln
        self.set_variables(index)

        #Text ausgeben
        self.print_frame()








