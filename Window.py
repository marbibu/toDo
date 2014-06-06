from Tkinter import Tk
class Window:
      #Klasa, ktora rysuje okno
      def __init__(s,title,w,h,x,y):
            #Dane:
            s.__title=title
            s.__w,s.__h=w,h
            s.__x,s.__y=x,y
            #Definicje:
            s.__draw()
      def __draw(s):#Rysuje okno
            s.__master=Tk()
            s.__master.title(s.__title)
            s.__master.geometry("%sx%s+%s+%s"%(s.__w,s.__h,s.__x,s.__y))
            s.__master.minsize(600, 600)
            s.__master.maxsize(600,0)
      def getTitle(s):#Zwraca tytul
            return s.__title
      def setTitle(s,title):#Ustawia tytul
            s.__title=title
            s.__master.title(title)
      def loop(s):#Zapetla wyswietlanie okna
            s.__master.mainloop()
      def getMaster(s):#Zwraca id okna
            return s.__master