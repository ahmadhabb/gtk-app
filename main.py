import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from app.controllers.app_controller import AppController
from app.controllers.dialog_media_controller import MediaDialogController
from app.models.dialog_media_model import DialogMediaModel
from pygrabber.dshow_graph import FilterGraph

class CameraController:
    """Controller to fetch available camera devices using pygrabber."""

    def __init__(self):
        self.dialog_media_model = DialogMediaModel()
        self.media_dialog_controller = MediaDialogController(self.dialog_media_model)

    def get_available_cameras(self):
        """Proxy method to fetch available cameras."""
        return self.media_dialog_controller.get_available_cameras()


if __name__ == "__main__":
    controller = CameraController()
    app = AppController(controller)  # Pass the controller with real camera data
    app.run()
    Gtk.main()
