class NoteManager:
      #mozna tylko dodawac
      def __init__(s):
            #Dane:
            s.__notes=[]
            s.__current=None
            s.__n=0
            s.__Y=10
      def addNote(s,note):#Dodaje notatke
            s.__notes.append(note)
            note.setY(s.__Y)
            s.selectNote(note)
            s.__n+=1
            s.__Y+=40
      def selectNote(s,note):#Zaznacza notatke
            if s.__current==None:
                  pass
            else:
                  s.__current.deselect()
            s.__current=note
            s.__current.select()
      def selectNext(s):#Zaznacza nastepna notatke
            if s.__current==None:
                  pass
            else:
                  ind=s.__notes.index(s.__current)
                  if ind<s.__n-1:
                        s.selectNote(s.__notes[ind+1])
                  else:
                        pass
      def selectPrevious(s):#Zaznacza poprzednia notatke
            if s.__current==None:
                  pass
            else:
                  ind=s.__notes.index(s.__current)
                  if ind>0:
                        s.selectNote(s.__notes[ind-1])
                  else:
                        pass
      def delNote(s):#Usuwa biezaca notatke
            if s.__current==None:
                  pass
            else:
                  ind=s.__notes.index(s.__current)
                  if ind==s.__n-1:
                        if ind==0:
                              s.__current=None
                        else:
                              s.__notes.remove(s.__current)
                              s.__current.destroy()
                              s.selectNote(s.__notes[ind-1])
                  else:
                        s.__notes.remove(s.__current)
                        s.__current.destroy()
                        s.selectNote(s.__notes[ind])
                        s.__updatePosition(ind)
                  s.__n-=1
                  s.__Y-=40
            
      def __updatePosition(s,index):#Odswieza pozycje notatek po usunieciu jednej z nich
            for i in s.__notes[index:]:
                  i.moveUp()
      def getCurrentNote(s):#Zwraca biezaca notatke
            return s.__current
      def hasNotes(s):#Sprawdza czy liste notatek nie jest pusta
            if s.__n>0:
                  return 1
            else:
                  return 0
      def hideAllNotes(s):#Ukrywa wszystkich potomkow
            for i in s.__notes:
                  i.hide()
      def showAllNotes(s):#Wyswietla wszystkich potomkow
            for i in s.__notes:
                  i.show()
      def getNotes(s):#Zwraca wszystkie notatki
            return s.__notes