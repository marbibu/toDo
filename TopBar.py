from Tkinter import Canvas
from Listener import Listener
class TopBar(Listener):
      def __init__(s,master,todo):
            #Dane:
            Listener.__init__(s)
            s.__master=master
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.listen2(todo)
      def __draw(s):#Rysuje kontrolke
            s.__C=Canvas(s.__master,highlightthickness=0,bg="gray70",height=100)
            s.__C.pack(side="top",expand=0,fill="x")
            s.__tag=s.__C.create_text(50,30,anchor="nw",width=500,text="")
      def __update(s):#Odswieza kontrolke
            text=s.__todo.getDominator().getText()
            s.__C.itemconfig(s.__tag,text=text)
      def receiveSignal(s,signal):#Odbiera sygnaly
            signalN=signal.getName()
            if signalN=="ToDo":
                  s.__update()