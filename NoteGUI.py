from Listener import Listener
from tkFont import Font
class NoteGUI(Listener):
      __nr=0
      __marginX=5
      __width=500
      __r=5
      def __init__(s,C,note):
            #Dane:
            Listener.__init__(s)
            s.__C=C
            s.__note=note
            s.__tag=s.__genTag()
            s.__font=Font(family="Monaco",size=14)
            #Definicje:
            s.__draw()
            s.__bind()
            s.listen2(note)
      def __genTag(s):#Generuje tag notatki
            s.__class__.__nr+=1
            return "Note%s"%s.__class__.__nr
      def __draw(s):#Rysuje
            x,y=s.__note.getXY()
            s.__C.create_rectangle(0,0,s.__width,30,fill="gray50",tag=(s.__tag,s.__tag+"bg"))
            s.__C.create_text(s.__marginX,15,text=s.__getText(s.__note.getText()),anchor="w",tag=(s.__tag,s.__tag+"text"),font=s.__font)
            s.__C.create_oval(-10-s.__r,15-s.__r,-10+s.__r,15+s.__r,width=2,fill="gray70",tag=(s.__tag,s.__tag+"select"),state="hidden")
            s.__C.create_polygon(s.__width+10,15-s.__r,s.__width+10,15+s.__r,s.__width+20,15,tag=(s.__tag,s.__tag+"children"),width=2,fill="gray70",outline="#000000",state="hidden")
            #co=s.__C.bbox(s.__tag+"text")
            
            #s.__C.lift(s.__tag+"text",s.__tag+"bg")
            #h=co[3]-co[1]
            #X,Y=x-10,y+0.5*h+s.__marginY
            
            #X,Y=x+500+5,y+0.5*h+s.__marginY
            
            #s.__note.setH(h+2*s.__marginY)
            
            
            s.__C.move(s.__tag,x,y)
            s.__update()
      def __getText(s,text):
            if len(text)>60:
                  return text[:54]+" [...]"
            else:
                  return text
      def __update(s):#Odswieza rysunek notatki
            s.__updateCoords()
            s.__updateVisible()
            #s.__updateChildren()
            s.__updateText()
            #s.__updateSelection()
      def __updateCoords(s):#Odswieza polozenie
            x,y=s.__note.getXY()
            s.__C.coords(s.__tag+"bg",0,0,s.__width,30)
            s.__C.coords(s.__tag+"text",s.__marginX,15)
            s.__C.coords(s.__tag+"select",-10-s.__r,15-s.__r,-10+s.__r,15+s.__r)
            s.__C.coords(s.__tag+"children",s.__width+10,15-s.__r,s.__width+10,15+s.__r,s.__width+20,15)
            s.__C.move(s.__tag,x,y)
            
      #def __updateSelection(s):#Odswieza zaznaczenie
      #      if s.__note.getVisible():
      #            if s.__note.getSelected()==1:
      #                  s.__C.itemconfig(s.__tag+"select",state="normal")
      #            else:
      #                  s.__C.itemconfig(s.__tag+"select",state="hidden")
      #      else:
      #            pass
      def __updateVisible(s):#Odswieza widocznosc
            if s.__note.getVisible():
                  s.__C.itemconfig(s.__tag,state="normal")
                  if s.__note.getSelected()==1:
                        s.__C.itemconfig(s.__tag+"select",state="normal")
                  else:
                        s.__C.itemconfig(s.__tag+"select",state="hidden")
                  if s.__note.hasChild():
                        s.__C.itemconfig(s.__tag+"children",state="normal")
                  else:
                        s.__C.itemconfig(s.__tag+"children",state="hidden")
            else:
                  s.__C.itemconfig(s.__tag,state="hidden")
      #def __updateChildren(s):#Odswieza wyswietlanie rozwiniecia
      #      if s.__note.hasChild():
      #            s.__C.itemconfig(s.__tag+"children",state="normal")
      #      else:
      #            s.__C.itemconfig(s.__tag+"children",state="hidden")
                  
                  
      def __updateText(s):#Odswieza tekst
            s.__C.itemconfig(s.__tag+"text",text=s.__getText(s.__note.getText()))
      def __click(s,event):#Klikniecie na notatke
            s.__note.getMaster().getManager().selectNote(s.__note)
      def __dclick(s,event):#Dwukrotne klikniecie na notatke
            print s.__note
            s.__note.getToDo().setDominator(s.__note)
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)
            s.__C.tag_bind(s.__tag,"<2>",s.__dclick)
      def receiveSignal(s,signal):#Odbiera sygnaly
            signalN=signal.getName()
            if signalN=="Note":
                  s.__update()