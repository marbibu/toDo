class Listener:
      #Klasa, ktora umozliwia odbieranie sygnalow od nadawcy
      def __init__(s):
            #Dane:
            pass
      def receiveSignal(s,sender):
            print "Nie zaimplementowano odbierania sygnalow"
      def listen2(s,sender):#Rozpoczyna nasluchiwanie wskazanego nadawcy
            sender.addListener(s)