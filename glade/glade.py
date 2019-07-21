#!usr/bin/env python
# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import random
#metodos
#--------------------------------------------------

def click(button):


    #Enllacem els objectes
    datoVel=random.randrange(11)/10
    labelVel= builder.get_object("labelVelocitat")
    barVel= builder.get_object("barVelocitat")
    
    labelVel.set_text(" "+str(datoVel*10)+" k/h")
   
   
    barVel.set_value(datoVel)
    
    datoTemp=random.randrange(11)/10
    labelTemp= builder.get_object("labelTemperatura")
    barTemp= builder.get_object("barTemperatura")
    
    labelTemp.set_text(" "+str(datoTemp*10)+" Cº")
    barTemp.set_value(datoTemp)
    
    datoRev=random.randrange(11)/10
    labelRev= builder.get_object("labelRevolucions")
    barRev= builder.get_object("barRevolucions") 
    
    
    labelRev.set_text(" "+str(datoRev)+" Rpm")
    labelRev.set_name('')
    barRev.set_value(datoRev)
    
    

#--------------------------------------------------
#creem el manipulador
builder = Gtk.Builder()
#indiquem el fitxer glade que utilitzem
builder.add_from_file("ejemplo.glade")
#Indiquem els  events i els relacionem
handlers={
    "pulsar": click,
    "terminar_aplicacion": Gtk.main_quit
    }



#conectem els events
builder.connect_signals(handlers)

#creem els objectes
windows=builder.get_object("ventana_principal")
#tamany de la finestara ample X alt
windows.set_default_size(1800, 600)

#mostrem la finestra ventana_principal
windows.show_all()
#mostrem el main
Gtk.main()
