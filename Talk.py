from Tkinter import Entry
from NoteGUI import NoteGUI
class Talk:
      def __init__(s,master,todo,desk):
            #Dane:
            s.__master=master
            s.__todo=todo
            s.__desk=desk
            #Definicje:
            s.__draw()
            s.__bind()
      def insertText(s,text):#Wstawia tekst
            s.__E.insert(0,text)
      def clean(s):#Czysci kontrolke
            s.__E.delete(0,"end")
      def __draw(s):#Rysuje kontrolke
            s.__E=Entry(s.__master,highlightthickness=0,relief="groove",bg="gray70",border=1,font=("Monaco",14),insertwidth=2)
            s.__E.pack(side="top",expand=0,fill="x",ipady=5)
      def __accept(s,event):#Akceptuje wprowadzony tekst
            text=s.__E.get()
            s.__todo.pushText(text)
            s.clean()
      def __selectAll(s,event):#Zaznacza wszytko co jest w entry
            s.__E.selection_range(0,"end")
      def __type(s,event):#pisanie w entry
            sym=event.keysym
            if sym=="Up" or sym=="Down" or sym=="Left" or sym=="Right":
                  if sym=="Up":
                        s.__todo.selectPrevious()
                  elif sym=="Down":
                        s.__todo.selectNext()
                  elif sym=="Left":
                        s.__todo.go2previousDominator()
                  elif sym=="Right":
                        s.__todo.setDominatorWithCurrentNote()
                  return 'break'
      def __addNewNote(s,event):#Dodaje nowa notatke
            note=s.__todo.addNote()
            NoteGUI(s.__desk.getC(),note)
      def __bind(s):#Tworzy bindowanie
            s.__E.focus_set()
            s.__E.bind("<Command-a>",s.__selectAll)
            s.__E.bind("<Command-t>",s.__addNewNote)
            s.__E.bind("<Return>",s.__accept)
            s.__E.bind("<KeyPress>",s.__type)