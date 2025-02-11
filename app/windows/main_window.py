import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from app.dialogs.media_source_dialog import MediaSourceDialog

class MainWindow(Gtk.Window):
    """Jendela utama aplikasi."""

    def __init__(self, controller):
        super().__init__(title="Fisheye Video Conference System")
        self.set_default_size(1440, 768)
        self.controller = controller

        # Main Layout
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Main Area
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        center_box.set_vexpand(True)
        self.main_area_label = Gtk.Label(label="Main Area")
        self.main_area_label.set_markup('<span foreground="#B3B3B3" font="20">Main Area</span>')
        self.main_area_label.set_alignment(0.5, 0.5)
        center_box.pack_start(self.main_area_label, True, True, 0)
        main_box.pack_start(center_box, True, True, 0)

        # Bottom Bar
        bottom_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        bottom_bar.set_margin_bottom(10)
        bottom_bar.set_margin_top(10)
        bottom_bar.set_margin_left(10)
        bottom_bar.set_margin_right(10)
        main_box.pack_end(bottom_bar, False, False, 0)

        # Add Button
        add_button = Gtk.Button(label="Tambah")
        add_button.set_size_request(100, 40)
        add_button.connect("clicked", self.on_add_button_clicked)
        bottom_bar.pack_start(add_button, False, False, 0)

        # Play Button
        play_button = Gtk.Button(label="")
        play_button.set_size_request(40, 40)
        play_button.set_tooltip_text("Start")
        play_button.set_image(Gtk.Image.new_from_icon_name("media-playback-start", Gtk.IconSize.BUTTON))
        play_button.connect("clicked", self.on_play_button_clicked)
        bottom_bar.pack_start(play_button, False, False, 0)

        # Mode Buttons
        modes = [
            ("Original Mode", "Original"),
            ("Discussion Mode", "Discussion"),
            ("Global Mode", "Global"),
            ("Patrol Mode", "Patrol"),
            ("Presentation", "Presentation"),
        ]
        for mode_label, mode_name in modes:
            mode_button = Gtk.Button(label=mode_label)
            mode_button.set_size_request(140, 40)
            mode_button.connect("clicked", self.on_mode_button_clicked, mode_name)
            mode_button.get_style_context().add_class("suggested-action") 
            bottom_bar.pack_start(mode_button, False, False, 0)

        # Limit Person Label and Dropdown
        limit_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        limit_label = Gtk.Label(label="Limit Person:")
        limit_box.pack_start(limit_label, False, False, 0)

        limit_dropdown = Gtk.ComboBoxText()
        for i in range(2, 13):
            limit_dropdown.append_text(str(i))
        limit_dropdown.set_active(0)
        limit_box.pack_start(limit_dropdown, False, False, 0)
        bottom_bar.pack_end(limit_box, False, False, 0)

        # Config Button
        config_button = Gtk.Button(label="Config")
        config_button.set_size_request(100, 40)
        config_button.get_style_context().add_class("suggested-action") 
        config_button.connect("clicked", self.on_config_button_clicked)
        bottom_bar.pack_end(config_button, False, False, 0)


    def on_add_button_clicked(self, button):
        """Tampilkan dialog MediaSourceDialog."""
        dialog = MediaSourceDialog(self.controller, self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            selected_values = dialog.get_selected_values()
            print(f"Perangkat terpilih: {selected_values}")
        else:
            print("Dialog dibatalkan")

        dialog.destroy()

    def on_play_button_clicked(self, button):
        print("Play Button Clicked!")

    def on_mode_button_clicked(self, button, mode_name):
        print(f"{mode_name} Mode Selected!")

    def on_config_button_clicked(self, button):
        print("Config Button Clicked!")
