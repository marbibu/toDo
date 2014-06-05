from NoteFactory import NoteFactory
from NoteGUI import NoteGUI
class AddOption:#Przerobic to na GUI
      #testowe
      def __init__(s,C,desk,todo):
            #Dane:
            s.__C=C
            s.__noteF=NoteFactory()
            s.__desk=desk
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.__bind()
            #s.__setDefaultNote()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(595,15,text="ADD",anchor="e")
      def __click(s,event):#Klikniecie
            dominator=s.__todo.getDominator()
            s.__noteF.newNote(s.__todo,dominator,50,0)
            note=s.__noteF.getNote()
            NoteGUI(s.__desk.getC(),note)
            dominator.addNote(note)
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)
#notatka przechowuje info o poprzedniej notatce, nastepnej,
#a takze o potomstwie
#addNote dodaje nastepna notatke

#todo powinien znac biezaca rozwinieta notatke


#add dodaje zawsze do biezacej/ dominujacej notatki