from Sender import Sender
from NoteManager import NoteManager
class Note(Sender,NoteManager):
      __marginY=10
      def __init__(s,master,text,x,y):
            #Dane:
            Sender.__init__(s)
            s.__noteM=NoteManager()
            s.__master=master
            s.__previous=None
            s.__next=None
            s.__text=text
            s.__x,s.__y=x,y
            s.__h=20
            s.__selected=0
            s.__visible=1
            s.__exist=1
      def getPrevious(s):#Zwraca id poprzednika
            return s.__previous
      def getNext(s):#Zwraca id nastepnika
            return s.__next
      def getMaster(s):#Zwraca nadrzednego
            return s.__master
      def getText(s):#Zwraca tekst
            return s.__text
      def getExist(s):#Zwraca parametr istnienia
            return s.__exist
      def getXY(s):#Zwraca polozenie notatki
            return s.__x,s.__y
      def getY(s):#Zwraca wspolrzedna y
            return s.__y
      def getH(s):#Zwraca wysokosc kontrolki
            return s.__h
      def getSelected(s):#Zwraca parametr zaznaczenia
            return s.__selected
      def getVisible(s):#Zwraca parametr widocznosci
            return s.__visible
      
      def setPrevious(s,note):#Ustawia poprzednika
            s.__previous=note
            s.sendSignal()
      def setNext(s,note):#Ustawia nastepnika
            s.__next=note
            s.__next.setPrevious(s)
            s.sendSignal()
      
      def setText(s,text):#Ustawia tekst
            s.__text=text
            s.sendSignal()
      
      def destroy(s):#Niszczy notatke
            s.__exist=0
            s.sendSignal()
      def create(s):#Tworzy notatke
            s.__exist==1
            s.sendSignal()
      
      def setY(s,y):#Ustawia polozenie notatki
            s.__y=y
            s.sendSignal()
      def setH(s,h):#Ustawia wysokosc kontrolki
            s.__h=h
            
      def select(s):#Zaznacza notatke
            s.__selected=1
            s.sendSignal()
      def deselect(s):#Odznacza notatke
            s.__selected=0
            s.sendSignal()
      
      def show(s):#Wyswietla notatke
            s.__visible=1
            s.sendSignal()
      def hide(s):#Ukrywa notatke
            s.__visible=0
            s.sendSignal()
      
      def addNote(s,note):#Dodaje notatke
            s.__noteM.addNote(note)
      
      def hasChild(s):#Zprawdza czy jest potomstwo
            return s.__noteM.hasNotes()
            #if s.__noteM.getFirst()==None:
                  #return 0
            #else:
                  #return 1
      #narazie mozna tylko dodawac do notatki