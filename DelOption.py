class DelOption:
      def __init__(s,C):
            #Dane:
            s.__C=C
            #Definicje:
            s.__draw()
            s.__bind()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(550,15,text="DEL",anchor="e")
      def __click(s,event):#Klikniecie
            print "Kliknieto na del"
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)