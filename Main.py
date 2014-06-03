from Window import Window
from Desk import Desk
from Talk import Talk
from ToDo import ToDo
from NoteFactory import NoteFactory
from NoteGUI import NoteGUI
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
            
            noteF=NoteFactory()
            noteF.newNote(None,50,50)
            note=noteF.getNote()
            note.setText("Jakis tam tekst")
            noteG=NoteGUI(C,note)
            #testowanie
            win.loop()
Main()