import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MediaSourceDialog(Gtk.Dialog):
    """Dialog untuk memilih perangkat kamera."""

    def __init__(self, controller, parent=None):
        super().__init__(title="Select Camera", transient_for=parent, flags=0)
        self.controller = controller
        self.set_default_size(300, 200)
        self.set_modal(True)

        # Variabel untuk perangkat yang dipilih
        self.selected_device_index = None

        # Box utama (konten dialog)
        box = self.get_content_area()
        box.set_spacing(10)

        # Judul dialog
        title_label = Gtk.Label(label="Camera Configuration")
        title_label.set_markup("<b>Camera Configuration</b>")
        title_label.set_justify(Gtk.Justification.CENTER)
        box.pack_start(title_label, False, False, 10)

        # Grid untuk input
        input_grid = Gtk.Grid()
        input_grid.set_column_spacing(10)
        input_grid.set_row_spacing(10)
        box.pack_start(input_grid, True, True, 0)

        # Label perangkat
        device_label = Gtk.Label(label="Device:")
        device_label.set_halign(Gtk.Align.END)
        input_grid.attach(device_label, 0, 0, 1, 1)

        # Dropdown untuk perangkat
        self.device_input = Gtk.ComboBoxText()
        self.populate_device_list()
        input_grid.attach(self.device_input, 1, 0, 1, 1)

        # Tombol Refresh
        refresh_button = Gtk.Button(label="Refresh")
        refresh_button.connect("clicked", self.on_refresh_clicked)
        input_grid.attach(refresh_button, 2, 0, 1, 1)

        # Tombol OK dan Cancel
        button_box = self.get_action_area()
        ok_button = Gtk.Button(label="OK")
        ok_button.connect("clicked", self.on_ok_clicked)
        button_box.pack_start(ok_button, True, True, 0)

        cancel_button = Gtk.Button(label="Cancel")
        cancel_button.connect("clicked", self.on_cancel_clicked)
        button_box.pack_start(cancel_button, True, True, 0)

        self.show_all()

    def populate_device_list(self):
        """Populate device list with available cameras."""
        available_devices = self.controller.get_available_cameras()
        self.device_input.remove_all()  # Bersihkan item sebelumnya

        if available_devices:
            for index, name in available_devices:
                self.device_input.append_text(f"{index} - {name}")
        else:
            self.device_input.append_text("No Camera Found")

    def on_refresh_clicked(self, button):
        """Handle tombol Refresh."""
        print("Refreshing device list...")
        self.populate_device_list()

    def on_ok_clicked(self, button):
        """Handle tombol OK."""
        active_index = self.device_input.get_active()
        if active_index >= 0:
            self.selected_device_index = active_index
            print(f"Selected Device Index: {self.selected_device_index}")
            self.response(Gtk.ResponseType.OK)
        else:
            print("No valid device selected.")

    def on_cancel_clicked(self, button):
        """Handle tombol Cancel."""
        self.response(Gtk.ResponseType.CANCEL)

    def get_selected_values(self):
        """Mengambil nilai perangkat yang dipilih."""
        return {"device_index": self.selected_device_index}
