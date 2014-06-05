from Sender import Sender
#from NoteFactory import NoteFactory
#from NoteGUI import NoteGUI
#import os
class ToDo(Sender):
      def __init__(s):
            #Dane:
            Sender.__init__(s)
            s.__dominator=None
            #Definicje:
      #def start(s):#Rozpoczyna dzialanie todo
            #s.read()
      def pushText(s,text):#Odbiera tekst
            current=s.__dominator.getCurrentChild()
            if current==None:
                  pass
            else:
                  current.setText(text)
      def setDominator(s,note):#Ustawia dominatora
            if s.__dominator==None:
                  pass
            else:
                  s.__dominator.hideChildren()
            s.__dominator=note
            s.__dominator.hide()
            s.__dominator.showChildren()
            s.sendSignal()
      def getDominator(s):#Pobiera dominatora
            return s.__dominator
      
            