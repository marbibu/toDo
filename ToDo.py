from Sender import Sender
class ToDo(Sender):
      def __init__(s):
            #Dane:
            Sender.__init__(s)
            s.__dominator=None
      def pushText(s,text):#Odbiera tekst
            print text
      def setDominator(s,note):#Ustawia dominatora
            s.__dominator=note
            s.__dominator.hide()
            s.sendSignal()
      def getDominator(s):#Pobiera dominatora
            return s.__dominator