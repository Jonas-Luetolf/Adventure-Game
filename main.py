
import handler as h



#main Funktion
def main():

    #erstellen von Framehandler
    frame_handler=h.handler("data.json")

    #laden des ersten Frames
    frame_handler.load_by_index("1")

    
    while True:

       
        ret=frame_handler.load_by_keyword((frame_handler.render.input()).lower())

        
        if ret=="END":
            break

    




if __name__=='__main__':
 
    #aufrufen von main Funktion
    main()
