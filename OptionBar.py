from Tkinter import Canvas
from PreviousOption import PreviousOption
from AddOption import AddOption
from DelOption import DelOption
from ReadOption import ReadOption
class OptionBar:
      def __init__(s,master,desk,todo):
            #Dane:
            s.__master=master
            #Definicje:
            s.__draw()
            s.__prevO=PreviousOption(s.__C,todo)
            s.__addO=AddOption(s.__C,desk,todo)
            s.__delO=DelOption(s.__C,todo)
            s.__readO=ReadOption(desk.getC(),todo)
      def __draw(s):#Rysuje kontrolke
            s.__C=Canvas(s.__master,highlightthickness=0,height=30,bg="gray70")
            s.__C.pack(side="top",expand=0,fill="x")
            