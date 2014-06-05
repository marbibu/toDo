from Note import Note
class NoteFactory:
      def __init__(s):
            #Dane:
            s.__note=None
      def newNote(s,todo,master,x,y):#Tworzy notatke
            s.__note=Note(todo,master,"Insert your text...",x,y)
      def firstNote(s,todo):#Tworzy pierwsza notatke
            s.__note=Note(todo,None,"ToDo",50,20)
      def newNoteWithText(s,todo,master,text,x,y):#Tworzy notatke z podanym tekstem
            s.__note=Note(todo,master,text,x,y)
      #def defaultNote(s):#Tworzy domyslna notatke
      def getNote(s):#Zwraca biezaca notatke
            return s.__note