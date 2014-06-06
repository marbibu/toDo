from NoteGUI import NoteGUI
class AddOption:#Przerobic to na GUI
      #testowe
      def __init__(s,C,desk,todo):
            #Dane:
            s.__C=C
            s.__desk=desk
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.__bind()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(595,15,text="ADD",anchor="e",activefill="gold")
      def __click(s,event):#Klikniecie
            note=s.__todo.addNote()
            NoteGUI(s.__desk.getC(),note)
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)
#notatka przechowuje info o poprzedniej notatce, nastepnej,
#a takze o potomstwie
#addNote dodaje nastepna notatke

#todo powinien znac biezaca rozwinieta notatke


#add dodaje zawsze do biezacej/ dominujacej notatki