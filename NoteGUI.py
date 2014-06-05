from Listener import Listener
class NoteGUI(Listener):
      __nr=0
      __marginX,__marginY=5,5
      __width=500
      __r=5
      def __init__(s,C,note):
            #Dane:
            Listener.__init__(s)
            s.__C=C
            s.__note=note
            s.__tag=s.__genTag()
            #Definicje:
            s.__draw()
            s.listen2(note)
      def __genTag(s):#Generuje tag notatki
            s.__class__.__nr+=1
            return "Note%s"%s.__class__.__nr
      def __draw(s):#Rysuje
            x,y=s.__note.getXY()
            s.__C.create_text(x+s.__marginX,y+s.__marginY,text=s.__note.getText(),width=s.__width-2*s.__marginX,anchor="nw",tag=(s.__tag,s.__tag+"text"))
            co=s.__C.bbox(s.__tag+"text")
            s.__C.create_rectangle(x,y,x+s.__width,co[3]+s.__marginY,fill="gray50",tag=(s.__tag,s.__tag+"bg"))
            s.__C.lift(s.__tag+"text",s.__tag+"bg")
            h=co[3]-co[1]
            X,Y=x-10,y+0.5*h+s.__marginY
            s.__C.create_oval(X-s.__r,Y-s.__r,X+s.__r,Y+s.__r,width=2,fill="gray70",tag=(s.__tag,s.__tag+"select"),state="hidden")
            X,Y=x+500+5,y+0.5*h+s.__marginY
            s.__C.create_polygon(X,Y+5,X,Y-5,X+10,Y,tag=(s.__tag,s.__tag+"children"),width=2,fill="gray70",outline="#000000")
            
            #s.__updateVisible()
            #s.__updateChildren()
            #s.__updateText()
            #s.__updateSelection()
            
            s.__note.setH(h+2*s.__marginY)
      def __update(s):#Odswieza rysunek notatki
            s.__updateCoords()
            s.__updateVisible()
            s.__updateChildren()
            s.__updateText()
            s.__updateSelection()
      def __updateCoords(s):#Odswieza polozenie
            x,y=s.__note.getXY()
            s.__C.coords(s.__tag+"text",x+s.__marginX,y+s.__marginY)
            co=s.__C.bbox(s.__tag+"text")
            print co
            s.__C.coords(s.__tag+"bg",x,y,x+s.__width,co[3]+s.__marginY)
            h=co[3]-co[1]
            X,Y=x-10,y+0.5*(h)+s.__marginY
            s.__C.coords(s.__tag+"select",X-s.__r,Y-s.__r,X+s.__r,Y+s.__r)
            X,Y=600+5,y+0.5*h+s.__marginY
            s.__C.coords(s.__tag+"children",X,Y+5,X,Y-5,X+10,Y)
            s.__note.setH(h+2*s.__marginY)
      def __updateSelection(s):#Odswieza zaznaczenie
            if s.__note.getSelected()==1:
                  print "widoczny"
                  s.__C.itemconfig(s.__tag+"select",state="normal")
            else:
                  print "ukryty"
                  s.__C.itemconfig(s.__tag+"select",state="hidden")
      def __updateVisible(s):#Odswieza widocznosc
            if s.__note.getVisible():
                  s.__C.itemconfig(s.__tag,state="normal")
            else:
                  s.__C.itemconfig(s.__tag,state="hidden")
      def __updateChildren(s):#Odswieza wyswietlanie rozwiniecia
            if s.__note.hasChild():
                  s.__C.itemconfig(s.__tag+"children",state="normal")
            else:
                  s.__C.itemconfig(s.__tag+"children",state="hidden")
      def __updateText(s):#Odswieza tekst
            s.__C.itemconfig(s.__tag+"text",text=s.__note.getText())
      def receiveSignal(s,signal):#Odbiera sygnaly
            signalN=signal.getName()
            if signalN=="Note":
                  s.__update()