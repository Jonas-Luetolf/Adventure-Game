import handler as h
import render as r
#main Funktion
def main():
    #erstellen von Framehandler
    frame_handler=h.handler("data.json",r)
    #laden des ersten Frames
    frame_handler.load_by_index("1")
    while True:
        if frame_handler.load_by_keyword((frame_handler.render.input()).lower()) == "END":
            break
if __name__=='__main__':
    main()
