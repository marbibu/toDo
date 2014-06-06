class PreviousOption:
      def __init__(s,C,todo):
            #Dane:
            s.__C=C
            s.__todo=todo
            #Definicje:
            s.__draw()
            s.__bind()
      def __draw(s):#Rysuje kontrolke
            s.__tag=s.__C.create_text(5,15,text="PREVIOUS",anchor="w",activefill="gold")
      def __click(s,event):#Klikniecie
            s.__todo.go2previousDominator()
      def __bind(s):#Tworzy bindowanie
            s.__C.tag_bind(s.__tag,"<1>",s.__click)