#-*- coding: utf-8 -*-
#-*- encoding: utf-8 -*-
from NoteFactory import NoteFactory
from NoteGUI import NoteGUI
import os
class ReadOption:
      def __init__(s,C,todo):
            #Dane:
            s.__C=C
            s.__todo=todo
            s.__noteF=NoteFactory()
            #Definicje:
            s.read()
      def read(s):#Wczytuje dane:
            if os.path.exists("./todo.txt"):
                  plik=open("./todo.txt","r")
                  dane=plik.readlines()
                  plik.close()
                  
                  s.__noteF.newNoteWithText(s.__todo,None,dane[0].rstrip().strip(),50,10)
                  note=s.__noteF.getNote()
                  NoteGUI(s.__C,note)
                  todo=note
                  current=note
                  for i in dane[1:]:
                        line=i.rstrip().strip()
                        if line=="<children>":
                              s.__todo.setDominator(current)
                        elif line=="</children>":
                              master=s.__todo.getDominator().getMaster()
                              if master==None:
                                    pass
                              else:
                                    s.__todo.setDominator(master)
                        else:
                              s.__noteF.newNoteWithText(s.__todo,s.__todo.getDominator(),line,50,10)
                              note=s.__noteF.getNote()
                              current=note
                              NoteGUI(s.__C,note)
                              s.__todo.getDominator().addNote(note)
                  s.__todo.setDominator(todo)
            else:
                  plik=open("./todo.txt","w")
                  plik.write("todo")
                  plik.flush()
                  plik.close()
                  s.read()
            