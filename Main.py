from Window import Window
from Desk import Desk
from Talk import Talk
from ToDo import ToDo
class Main:
      def __init__(s):
            #Dane:
            win=Window("todo",600,600,0,0)
            master=win.getMaster()
            desk=Desk(master)
            C=desk.getC()
            todo=ToDo()
            
            talk=Talk(master,todo)
            #testowanie
            #testowanie
            win.loop()
Main()