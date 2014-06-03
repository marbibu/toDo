from Note import Note
class NoteFactory:
      def __init__(s):
            #Dane:
            s.__note=None
      def newNote(s,master,x,y):#Tworzy notatke
            s.__note=Note(master,"",x,y)
      def getNote(s):#Zwraca biezaca notatke
            return s.__note