from Listener import Listener
class NoteGUI(Listener):
      __nr=0
      __marginX,__marginY=5,5
      __width=500
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
            s.__note.setH(co[3]-co[1])
      def __update(s):#Odswieza rysunek notatki
            s.__updateCoords()
            #s.__update
      def __updateCoords(s):#Odswieza polozenie
            x,y=s.__note.getXY()
            s.__C.coords(s.__tag+"text",x+s.__marginX,y+s.__marginY,text=s.__note.getText())
            co=s.__C.bbox(s.__tag+"text")
            s.__C.coords(s.__tag+"bg",x,y,x+s.__width,co[3]+s.__marginY)
            s.__note.setH(co[3]-co[1])
      def receiveSignal(s,signal):#Odbiera sygnaly
            signalN=signal.getName()
            if signalN=="Note":
                  s.__update()