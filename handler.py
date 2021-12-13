import json

class handler:
    def __init__(self,path,render):
        #öffnen von json
        with open(path,"r") as f:
            self.data=json.load(f)   
        self.render=render.render()
        #erstellen von Variabeln
        self.frame_data=""
        self.next_frame_data=""
        self.text_color=""
        self.text_data=""

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
    
    def load_by_keyword(self,action):
        try:
            #laden von neuem frameindex
            index=self.next_frame_data[action]
            if self.next_frame_data[action] =="END":
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

    def load_by_index(self,index):
        #setzen der Variabeln
        self.set_variables(index)
        #Text ausgeben
        self.print_frame()
