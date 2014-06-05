from NoteFactory import NoteFactory
from NoteGUI import NoteGUI
class AddOption:#Przerobic to na GUI
      #testowe
      __nr=0
      
      def __init__(s,C,desk,todo):
            #Dane:
            s.__C=C
            s.__noteF=NoteFactory()
            s.__desk=desk
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.__bind()
            s.__setDefaultNote()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(595,15,text="ADD",anchor="e")
      def __setDefaultNote(s):#Ustawia domyslna opcje
            s.__noteF.newNoteWithText(None,"ToDo",50,10)
            note=s.__noteF.getNote()
            NoteGUI(s.__desk.getC(),note)
            s.__todo.setDominator(note)
            print "Ustawiono domyslna wartosc dla biezacego dominatora"
      def __click(s,event):#Klikniecie
            
            s.__class__.__nr+=1
            
            dominator=s.__todo.getDominator()
            s.__noteF.newNote(dominator,50,0)
            note=s.__noteF.getNote()
            NoteGUI(s.__desk.getC(),note)
            dominator.addNote(note)
            
            #print current,dominator.getCurrentNote()
            
            note.setText("tekst %s"%s.__class__.__nr)
                        
                  #print "biezaca grubosc %s"%note.getH()
                  
            
            
            
            #dominator.addNote(note)
            #if dominator==None:
                  
            #currentNote=s.__todo.getCurrentNote()
            
            #if currentNote==None:
            
            #
            #s.__todo.addNote(note)
            
            
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)

#notatka przechowuje info o poprzedniej notatce, nastepnej,
#a takze o potomstwie
#addNote dodaje nastepna notatke

#todo powinien znac biezaca rozwinieta notatke


#add dodaje zawsze do biezacej/ dominujacej notatki