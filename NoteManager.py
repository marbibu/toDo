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
      def selectNote(s,note):#Zaznacza notatke
            if s.__current==None:
                  pass
            else:
                  s.__current.deselect()
            s.__current=note
            s.__current.select()
            s.__n+=1
            s.__Y+=s.__current.getH()+10
            print s.__current.getSelected()
      def delNote(s):#Usuwa biezaca notatke
            ind=s.__notes.index(s.__current)
            if ind==s.__n:
                  if ind==0:
                        s.__current=None
                  else:
                        s.selectNote(s.__notes[ind-1])
            else:
                  s.selectNote(s.__notes[ind+1])
            s.__notes.remove(s.__current)
            s.__n-=1
      def getCurrentNote(s):#Zwraca biezaca notatke
            return s.__current
      def hasNotes(s):#Sprawdza czy liste notatek nie jest pusta
            if s.__n>0:
                  return 1
            else:
                  return 0