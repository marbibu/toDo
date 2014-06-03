class Sender:
      #Klasa, ktora rozsyla info do odbiorcow
      def __init__(s):
            #Dane:
            s.__listeners=[]
      def addListener(s,listener):#Dodaje sluchacza
            s.__listeners.append(listener)
      def delListener(s,listener):#Usuwa sluchacza
            s.__listeners.remove(listener)
      def sendSignal(s):#Wysyla sygnal
            for i in s.__listeners:
                  i.receiveSignal(s)
      def getName(s):#Zwraca nazwe nadawcy
            return s.__class__.__name__