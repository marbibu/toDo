from Tkinter import Entry
class Talk:
      def __init__(s,master,todo):
            #Dane:
            s.__master=master
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.__bind()
      def insertText(s,text):#Wstawia tekst
            s.__E.insert(0,text)
      def clean(s):#Czysci kontrolke
            s.__E.delete(0,"end")
      def __draw(s):#Rysuje kontrolke
            s.__E=Entry(s.__master,highlightthickness=0,relief="flat")
            s.__E.pack(side="top",expand=0,fill="x")
      def __accept(s,event):#Akceptuje wprowadzony tekst
            text=s.__E.get()
            print text
            s.__todo.pushText(text)
            s.clean()
      def __preview(s,event):#Wysyla podglad
            text=s.__E.get()
            s.__todo.pushText(text)
      def __selectAll(s,event):#Zaznacza wszytko co jest w entry
            s.__E.selection_range(0,"end")
      def __bind(s):#Tworzy bindowanie
            s.__E.focus_set()
            s.__E.bind("<Command-a>",s.__selectAll)
            s.__E.bind("<Return>",s.__accept)
            s.__E.bind("<Any-KeyRelease>",s.__preview)