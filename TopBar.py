from Tkinter import Canvas
class TopBar:
      def __init__(s,master):
            #Dane:
            s.__master=master
            s.__text="Domyslny tekst"
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje kontrolke
            s.__C=Canvas(s.__master,highlightthickness=0,bg="gray70",height=100)
            s.__C.pack(side="top",expand=0,fill="x")
            s.__tag=s.__C.create_text(50,30,anchor="nw",width=500,text=s.__text)
      def setText(s,text):#Ustawia tekst tytulu
            s.__text=text