from Tkinter import Canvas
class Desk:
      #Klasa, ktora rysuje Desk
      def __init__(s,master):
            #Dane:
            s.__master=master
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje Canvas
            s.__C=Canvas(s.__master,highlightthickness=0,bg="gray80")
            s.__C.pack(side="top",expand=1,fill="both")
      def getC(s):#Zwraca id Canvasu
            return s.__C