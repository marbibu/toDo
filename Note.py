from Sender import Sender
class Note(Sender):
      def __init__(s,master,text):
            #Dane:
            Sender.__init__(s)
            s.__master=master
            s.__previous=None
            s.__next=None
            s.__text=text
            s.__selected=1
      def setPrevious(s,note):#Ustawia poprzednika
            s.__previous=note
            s.sendSignal()
      def setNext(s,note):#Ustawia nastepnika
            s.__next=note
            s.sendSignal()
      def getPrevious(s):#Zwraca id poprzednika
            return s.__previous
      def getNext(s):#Zwraca id nastepnika
            return s.__next
      def getMaster(s):#Zwraca nadrzednego
            return s.__master
      def getText(s):#Zwraca tekst
            return s.__text
      def setText(s,text):#Ustawia tekst
            s.__text=text
            s.sendSignal()
      def select(s):#Zaznacza notatke
            s.__selected=1
            s.sendSignal()
      def deselect(s):#Odznacza notatke
            s.__selected=0
            s.sendSignal()
      def getSelected(s):#Zwraca parametr zaznaczenia
            return s.__selected
            