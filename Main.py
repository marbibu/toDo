from Window import Window
from Desk import Desk
from Talk import Talk
from ToDo import ToDo
from NoteFactory import NoteFactory
from NoteGUI import NoteGUI
from TopBar import TopBar
from OptionBar import OptionBar

class Main:
      def __init__(s):
            #Dane:
            win=Window("todo",600,600,0,0)
            master=win.getMaster()
            todo=ToDo()
            
            topB=TopBar(master,todo)
            desk=Desk(master)
            C=desk.getC()
            
            optionB=OptionBar(master,desk,todo)
            talk=Talk(master,todo)
            #testowanie
            
            
            #testowanie
            win.loop()
Main()
#swift

