from Window import Window
from Talk import Talk
class Main:
      def __init__(s):
            #Dane:
            win=Window("todo",600,600,0,0)
            master=win.getMaster()
            desk=Desk(master)
            C=desk.getC()
            #testowanie
            #testowanie
            win.loop()
Main()