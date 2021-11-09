# Adventure Game Informatikprojekt SJ 21/22:



## Datenspeicherung in json:
``` json
"1":{
     "text":"<Text einfügen>"
     "next":{"<keyword zum nächsen Frame>":"<index>"},
     "color":"<Textfarbe>"
     

     }
```
 Die einzelnen Frames werden als json Objekte gespeichert, der eintrag "next" ist auch ein Objekt und kann belibig viele Elemeint enthalten. Das Keyword wird bei der Eingabe des Benutzers eingegeben und kann auch "" sein wenn nur die Taste <Return> gedrückt werden soll.
 Das Endframe erhält den Eintrag
 ```
 "next":{"":"END"}
 ```
 Als Textfarben stehen "green","red","orange" und "white" zur verfügung.  
 
 

 
## Render-Klasse:

### Imports:
- time
- os
- sys


### Methoden:

|Name:|Parameter:|
|---|---|
|Konstuktor|--|
|"clear"|--|
|"print"|Text und Textfarbe|
|"input"|--|


#### Konstruktor
Der Konstruktor erstellt ein Dictionary in dem die einzelnen Farbcodes mit ihren dazugehörigen Namen gespeichert sind.
``` python
self.colors={"green":'\033[92m',
             "orange":'\033[93m',
             "red":'\033[91m',
             "white":'\033[0m'}
```

#### "clear" Methode:
Die clear Methode ist für Windows, Linux, MacOs geeignet, sie ruft auf dem Modul "os" die Methode "system" auf und übergibt "cls"(Windows) oder "clear"(Linux,MacOs), diese löscht einfach alle Zeichen auf der Konsole.

#### "print" Methode:
Die print Methode gibt den übergebenen Text Zeichen weise mit einem abstand von 0.015s aus, dies geschiet über die Funktion sys.stdout.write() zwischen den zeichen muss der Buffer dur sys.stdout.flusch() geleert werden.

#### "input" Methode:
Die input methode gibt den Eingegebenen Text zurück. Dies geschieht über die builtin Funktion input().



## Handler:
### Imports:
- json
- render

### Methoden
|Name:|Parameter:|
|---|---|
|Konstruktor|Pfad zur Json Datei|
|"load_by_index"|Index des ersten Frames als String|
|"load_by_keywoard"|Keyword zum nächsten Frame|
|"set_variables"|Index als String|
|"print_frame"|---|

#### Konstruktor 
Dem Konstuktor wird der Pfad zur Json Datei übergeben, in der Die Frames gespeichert sind.
Der Konstruktor öffnet die Datei und lädt den Inhalt ,mit der Methode load() auf dem Modul Json, in die Variable self.data. Zudem wird eiene Instanz der Renderklasse in self.render gespeichert.

#### "load_by_index" Methode:
Der Methode load_by_index wird ein Index, als String, übergeben. Die Methode weisst der Variable self.frame_data das ganze Jsonobjekt hinter dem Index zu und ruft die Mehoden print_frame und set_Variables auf dem Handler auf.

#### "set_variables" Methode:
Die Variabeln self.frame_data, self.next_frame_data, self.text_data und self.text_color werden mit dem übergebenen Index auf die neuen Werte gesetzt.

#### "print_frame" Methode:
Die Methode ruft die Methode "clear" auf der Renderinstanz "self.render" auf und übergibt der Methode "print" auf der Renderinstanz "self.render" die Variablen self.text_data und self.text_color.

## Main Funktion:


``` python
def main():

    frame_handler=h.handler("data.json")

    frame_handler.load_by_index("1")

    while True:

        ret=frame_handler.load_by_keywoard(frame_handler.render.input())

        if ret=="END":
            break

```

Zuerst wird eine Instanz der Klasse handler erstellt und der Pfad der Datei "data.json" dem Konstruktor übergeben. Danach wird das erste Frame mit dem Index "1" geladen.
Danach wird in einer unendlichschleife das nächste Frame geladen, Das Keyword wird durch die Renderinstanz, die im Handler gespeichert ist mit der Methode input ausgelesen. Der Rückgabewert der Methode load_by_keywoard auf dem frame_handler wird in der Variable ret gespeichert, es wird überprüft ob der Wert "END" ist, falls ja, springt das Programm aus dem loop und beendet sich automatisch.

## Aufbau

Das Programm ist so aufgebaut, dass der Code möglichst Wenig widerholungen hat. So habe ich z.B. die Funktion input nur einmal verwendet. Ich habe den Code auch so gestalltet, dass die Json Datei und nicht das Programm vorgibt wie das Game abläuf und bei einem anderen gleich Aufgebauten Spiel nur die Json Datei Verändert werden muss. Das Programm ist im Grunde genommen mit zwei Klassen aufgebaut, so sind die Aufgaben gut von einander getrent sind.


## Wie bin ich auf die Idee gekommen und wie habe ich den Code entwickelt?

Ich hatte das Ziel den Code so allgemein wie möglich zu gestallten. Der Code sollt auch effizient sein und keine unnötige Variabeln haben.
Zuerst habe ich mir überlegt wie ich den Code gestallten will. Ich bin schnell auf die Idee gekommen eine Json Datei mit den Frames zu machen. Dann habe ich mir überlegt wie ich den Code gut unterteilen konnte.Die Handler-Klasse habe ich zuerst entwickelt, ich brauche eine Funktion die immer das Nächst Frame lädt, später ist mir aufgefallen das ich zum laden des ersten Frames eine andere vogehensweise benötige, daraus ist diese Funktion entstanden. Danach habe ich die Render-Klasse eintwickelt, zuerst konnte sie nur Text anzeigen, später habe ich noch die Animation eingabaut und eine input Methode erstellt, diese ist in diesem Fall eher Unnötig da man in der Main Funktion auch einfach die builtin Funktion input aufrufen hätte können, doch wenn man z.B. ein GUI implementiert muss man die Main Funktion nicht verändern. 

Probleme hatte ich egentlich keine und den Code hatte ich auch schnell eintwickelt, aber das einfüten der Texte war mühsam da mann immer die vielen Klammern und doppelpunkte schreiben musst und alle doppelten Anführungszeichen durch einfach ersetzen musste.

