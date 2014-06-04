class PreviousOption:
      def __init__(s,C):
            #Dane:
            s.__C=C
            #Definicje:
            s.__draw()
            s.__bind()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(5,15,text="PREVIOUS",anchor="w")
      def __click(s,event):#Klikniecie
            print "Kliknieto na previous"
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)