import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="Hola Món")
        self.box = Gtk.Box(spacing=29)
        self.add(self.box)
        
        self.label = Gtk.Label(label="Hello World")
        self.box.pack_start(self.label,True,True,0)
        
        
        self.button= Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.box.pack_start(self.button,True,True,0)

        

    def on_button_clicked(self, widget):
        print("Hola Món")

window= MyWindow()
window.connect("destroy",Gtk.main_quit)
window.set_default_size(600, 400)

window.show_all()
Gtk.main()
