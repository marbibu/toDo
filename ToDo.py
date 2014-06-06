#-*- coding: utf-8 -*-
#-*- encoding: utf-8 -*-
from Sender import Sender
from NoteFactory import NoteFactory
import codecs
class ToDo(Sender):
      def __init__(s):
            #Dane:
            Sender.__init__(s)
            s.__dominator=None
            s.__saveString=""
            s.__noteF=NoteFactory()
      def pushText(s,text):#Odbiera tekst
            current=s.__dominator.getCurrentChild()
            if current==None:
                  pass
            else:
                  if text=="<children>" or text=="/children" or text=="":
                        pass
                  else:
                        current.setText(text)
                        s.__save()
      def setDominator(s,note):#Ustawia dominatora
            if note==None:
                  pass
            else:
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
      def addNote(s):#Dodaje notatke do dominatora
            s.__noteF.newNote(s,s.__dominator,50,0)
            note=s.__noteF.getNote()
            s.__dominator.addNote(note)
            s.__save()
            return note
      def delNote(s):#Usuwa biezaca notatke od dominatora
            s.__dominator.delNote()
            s.__save()
      def add2saveString(s,string):#Dodaje do stringu
            s.__saveString+=string
      def __getToDoNote(s):#Zwraca id glownej notatki
            note=s.__dominator
            while note.getMaster()!=None:
                  note=note.getMaster()
            return note
      def __prepareString(s,text):#Przygotowuje napis do zapisu
            text=text.encode("utf-8")
            return text.decode("utf-8")
      def __save(s):#Zapisywanie
            s.__getToDoNote().getString(0)
            plik=codecs.open("./todo.txt", 'w', 'utf-8')
            plik.write(s.__prepareString(s.__saveString))
            plik.flush()
            plik.close()
            s.__saveString=""
      def selectNext(s):#Zaznacz nastepna notatke w dominatorze
            s.__dominator.getManager().selectNext()
      def selectPrevious(s):#Zaznacza poprzednia notatke w dominatorze
            s.__dominator.getManager().selectPrevious()
      def go2previousDominator(s):#Wraca do poprzedniego dominatora
            master=s.__dominator.getMaster()
            if master==None:
                  pass
            else:
                  s.setDominator(master)
      def setDominatorWithCurrentNote(s):#Ustawia na dominatora biezaca notatke
            s.setDominator(s.__dominator.getManager().getCurrentNote())