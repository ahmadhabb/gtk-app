import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from app.controllers.app_controller import AppController

class DummyController:
    """Controller dummy untuk simulasi."""
    @staticmethod
    def get_available_cameras():
        return [(0, "Camera 1"), (1, "Camera 2"), (2, "Camera 3")]

if __name__ == "__main__":
    controller = DummyController()
    app = AppController(controller)  # Berikan controller
    app.run()
    Gtk.main()
