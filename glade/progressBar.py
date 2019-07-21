import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self,title="ProgressBar")
       
        self.progressBar= Gtk.LevelBar()
        self.progressBar.set_text("0.20")
      
        self.progressBar.set_show_text(True)

        self.add(self.progressBar)

window= MyWindow()
window.connect("destroy",Gtk.main_quit)
window.set_default_size(600, 400)

window.show_all()
Gtk.main()
