from Tkinter import Canvas
class Desk:
      #Klasa, ktora rysuje Desk
      def __init__(s,master):
            #Dane:
            s.__master=master
            #Definicje:
            s.__draw()
            s.__bind()
      def __draw(s):#Rysuje Canvas
            s.__C=Canvas(s.__master,highlightthickness=0,bg="gray80")
            s.__C.pack(side="top",expand=1,fill="both")
      def getC(s):#Zwraca id Canvasu
            return s.__C
      def __click(s,event):#Klikniecie
            co=s.__C.bbox("all")
            if co==None:
                  pass
            else:
                  s.__C.config(scrollregion=(co[0],10,co[2],co[3]))
      def __scroll(s,event):#Przewijanie
            x,y=event.x,event.y
            s.__C.scan_mark(x,y)
            s.__C.scan_dragto(x,y+event.delta,gain=4)
      def __bind(s):#Tworzy bindowanie
            s.__C.bind("<1>",s.__click)
            s.__C.bind("<MouseWheel>",s.__scroll)