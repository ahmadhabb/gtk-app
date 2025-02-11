import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from app.windows.main_window import MainWindow

class AppController:
    def __init__(self, controller):
        # Pastikan controller diteruskan ke MainWindow
        self.window = MainWindow(controller)

    def run(self):
        self.window.show_all()
