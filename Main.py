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
            
            
            
            #nF=NoteFactory()
            #nF.firstNote()
            #note=nF.getNote()
            #nG=NoteGUI(C,note)
            #note.deselect()
            #print note.getSelected()
            #current=note
            
            #nF.newNote(None,50,current.getY(0))
            #note2=nF.getNote()
            #NoteGUI(C,note2)
            #current=note
            
            #note.hide()
            
            #noteF.newNote(None,50,50)
            #note=noteF.getNote()
            #note.setText("Jakis tam tekst,Jakis tam tekst,Jakis tam tekst,Jakis tam tekst,,Jakis tam tekst,Jakis tam tekst,Jakis tam tekst,Jakis tam tekst,Jakis tam tekst")
            #noteG=NoteGUI(C,note)
            
            
            #note.getH()
            #testowanie
            win.loop()
Main()
#swift

#ADD dodaje notatke do tytulowej notatki
#INS dodaje notatke do biezacej notatki
#INS nie bedzie potrzebny...
#