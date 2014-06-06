from Sender import Sender
from NoteManager import NoteManager
from copy import deepcopy
class Note(Sender,NoteManager):
      __marginY=10
      def __init__(s,todo,master,text,x,y):
            #Dane:
            Sender.__init__(s)
            s.__noteM=NoteManager()
            s.__todo=todo
            s.__master=master
            s.__text=text
            s.__x,s.__y=x,y
            s.__h=20
            s.__selected=0
            s.__visible=1
            s.__exist=1
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
      def getMaster(s):#Zwraca mastera
            return s.__master
      def getManager(s):#Zwraca managera
            return s.__noteM
      def getCurrentChild(s):#Zwraca biezacego potomka
            return s.__noteM.getCurrentNote()
      def showChildren(s):#Wyswietla potomstwo
            s.__noteM.showAllNotes()
      def hideChildren(s):#Ukrywa potomstwo
            s.__noteM.hideAllNotes()
      def getToDo(s):#Zwraca todo
            return s.__todo
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
      def delNote(s):#Usuwa notatke
            s.__noteM.delNote()
      def hasChild(s):#Sprawdza czy jest potomstwo
            return s.__noteM.hasNotes()
      def getString(s,t):#Zwraca string z zapisem
            s.__todo.add2saveString("%s%s\n"%(t*"\t",s.__text))
            notes=s.__noteM.getNotes()
            if len(notes)==0:
                  pass
            else:
                  s.__todo.add2saveString("%s<children>\n"%(t*"\t"))
                  t+=1
                  for i in notes:
                        i.getString(t)
                  s.__todo.add2saveString("%s</children>\n"%((t-1)*"\t"))
      def moveUp(s):#Przemieszcza notatke do gory o jej wysokosc
            s.setY(s.__y-40)
                  