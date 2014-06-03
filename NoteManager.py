class NoteManager:
      def __init__(s):
            #Dane:
            s.__first=None
            s.__current=None
      def addNote(s,note):#Dodaje
            #s.__note.append(note)
            if s.__first==None:
                  s.__first=note
            else:
                  pass
            s.__current.setNext(note)
            s.selectNote(note)
      def selectNote(s,note):#Zaznacza
            if s.__note==None:
                  pass
            else:
                  s.__note.deselect()
            s.__current=note
            s.__current.select()
      def delNote(s):#Usuwa
            prev=s.__current.getPrevious()
            nex=s.__current.getNext()
            s.__current.destroy()
            if s.__first==s.__current:
                  if nex==None:
                        s.__first=None
                  else:
                        s.__first=nex
            else:
                  pass
            if prev==None:
                  if nex==None:
                        s.__current=None
                  else:
                        nex.setPrevious(None)
                        s.selectNode(nex)
            else:
                  if nex==None:
                        prev.setNext(None)
                        s.selectNode(prev)
                  else:
                        prev.setNext(nex)
                        s.select(nex)
      def getCurrentNote(s):#Zwraca biezaca notatke
            return s.__current