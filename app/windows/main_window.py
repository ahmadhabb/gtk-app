import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from app.dialogs.media_source_dialog import MediaSourceDialog

class MainWindow(Gtk.Window):
    """Main application window."""

    def __init__(self, controller):
        super().__init__(title="Fisheye Video Conference System")
        self.set_default_size(1440, 768)
        self.controller = controller

        # Main Layout
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(main_box)

        # Horizontal Box for Sidebar and Main Area
        content_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        main_box.pack_start(content_box, True, True, 0)

        # Sidebar Revealer
        self.sidebar_revealer = Gtk.Revealer()
        self.sidebar_revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_RIGHT)
        self.sidebar_revealer.set_transition_duration(300)
        self.sidebar_revealer.set_reveal_child(False)

        # Sidebar Content
        self.sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.sidebar_box.set_size_request(300, -1)
        self.sidebar_box.set_margin_top(10)
        self.sidebar_box.set_margin_bottom(10)
        self.sidebar_box.set_margin_left(10)
        self.sidebar_box.set_margin_right(10)

        # Wrap the sidebar_box with Gtk.Frame to add a border
        sidebar_frame = Gtk.Frame()
        sidebar_frame.set_shadow_type(Gtk.ShadowType.ETCHED_IN)  # Set the type of shadow/border
        sidebar_frame.add(self.sidebar_box)

        self.sidebar_revealer.add(sidebar_frame)  # Add the frame to the revealer
        content_box.pack_start(self.sidebar_revealer, False, False, 0)

        # Identify Camera Section
        identify_camera_button = Gtk.Button()
        identify_camera_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        identify_camera_icon = Gtk.Image.new_from_icon_name("camera-web-symbolic", Gtk.IconSize.BUTTON)
        identify_camera_label = Gtk.Label(label="Identify Camera")
        identify_camera_box.pack_start(identify_camera_icon, False, False, 0)
        identify_camera_box.pack_start(identify_camera_label, False, False, 0)
        identify_camera_button.add(identify_camera_box)
        self.sidebar_box.pack_start(identify_camera_button, False, False, 10)

        # Placement Camera Section
        placement_camera_label = Gtk.Label(label="Placement Camera")
        placement_camera_label.set_markup('<span font="16" weight="bold">Placement Camera</span>')
        self.sidebar_box.pack_start(placement_camera_label, False, False, 0)

        placement_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        
        # Camera Toggle Button
        self.camera_toggle_button = Gtk.Button(label="Camera Downside")
        self.camera_toggle_button.set_size_request(140, 40)
        self.camera_toggle_button.get_style_context().add_class("destructive-action")  # Default red (OFF)
        self.camera_toggle_button.connect("clicked", self.on_camera_toggle_button_clicked)

        placement_box.pack_start(self.camera_toggle_button, True, True, 0)
        self.sidebar_box.pack_start(placement_box, False, False, 0)

        # View List Section
        self.view_list_label = Gtk.Label(label="View List")
        self.view_list_label.set_markup('<span font="16" weight="bold">View List</span>')
        self.sidebar_box.pack_start(self.view_list_label, False, False, 0)

        self.view_list_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.sidebar_box.pack_start(self.view_list_box, False, False, 0)

        self.sidebar_revealer.add(self.sidebar_box)
        content_box.pack_start(self.sidebar_revealer, False, False, 0)

        # Main Content Area
        center_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        center_box.set_vexpand(True)

        # Menambahkan gambar dari folder assets
        self.image = Gtk.Image()
        self.image.set_from_file("../assets/moil.jpg")  # Ganti dengan nama file gambar yang benar

        # Menambahkan gambar ke dalam box
        center_box.pack_start(self.image, True, True, 0)

        # Menambahkan ke content_box
        content_box.pack_start(center_box, True, True, 0)

        # Bottom Bar
        self.bottom_bar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.bottom_bar.set_margin_bottom(10)
        self.bottom_bar.set_margin_top(10)
        self.bottom_bar.set_margin_left(10)
        self.bottom_bar.set_margin_right(10)
        main_box.pack_end(self.bottom_bar, False, False, 0)

        # Add Button
        add_button = Gtk.Button(label="Add Resource")
        add_button.set_size_request(100, 40)
        add_button.get_style_context().add_class("suggested-action") 
        add_button.connect("clicked", self.on_add_button_clicked)
        self.bottom_bar.pack_start(add_button, False, False, 0)

        # Play Button
        play_button = Gtk.Button()
        play_button.set_size_request(40, 40)
        play_button.get_style_context().add_class("suggested-action") 
        play_button.set_tooltip_text("Start")
        play_icon = Gtk.Image.new_from_icon_name("media-playback-start", Gtk.IconSize.BUTTON)
        play_button.set_image(play_icon)
        play_button.connect("clicked", self.on_play_button_clicked)
        self.bottom_bar.pack_start(play_button, False, False, 0)

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
            self.bottom_bar.pack_start(mode_button, False, False, 0)

        # Limit Person Label and Dropdown
        limit_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        limit_label = Gtk.Label(label="Limit Person:")
        limit_box.pack_start(limit_label, False, False, 0)

        self.limit_dropdown = Gtk.ComboBoxText()
        for i in range(2, 13):
            self.limit_dropdown.append_text(str(i))
        self.limit_dropdown.set_active(0)
        self.limit_dropdown.connect("changed", self.on_limit_dropdown_changed)
        limit_box.pack_start(self.limit_dropdown, False, False, 0)
        self.bottom_bar.pack_end(limit_box, False, False, 0)

        # AI Toggle Button
        self.ai_toggle_button = Gtk.Button(label="AI Tracking (OFF)")
        self.ai_toggle_button.set_size_request(140, 40)
        self.ai_toggle_button.get_style_context().add_class("destructive-action")  # Default red (OFF)
        self.ai_toggle_button.connect("clicked", self.on_ai_toggle_button_clicked)
        self.bottom_bar.pack_end(self.ai_toggle_button, False, False, 0)

        # Config Button
        config_button = Gtk.Button(label="Config")
        config_button.set_size_request(100, 40)
        config_button.get_style_context().add_class("suggested-action") 
        config_button.connect("clicked", self.on_config_button_clicked)
        self.bottom_bar.pack_end(config_button, False, False, 0)

        # Panorama Button (initially hidden)
        self.panorama_toggle_button = Gtk.Button(label="Panorama (OFF)")
        self.panorama_toggle_button = Gtk.Button(label="Panorama")
        self.panorama_toggle_button.set_size_request(140, 40)
        self.panorama_toggle_button.connect("clicked", self.on_panorama_toggle_button_clicked)
        self.panorama_toggle_button.get_style_context().add_class("suggested-action")
        self.panorama_toggle_button.set_visible(False)  # Initially hidden
        print("Panorama button initialized and hidden")  # Log untuk debugging

        self.panorama_toggle_button.connect("clicked", self.on_panorama_button_clicked)
        self.bottom_bar.pack_start(self.panorama_toggle_button, False, False, 0)

    def on_add_button_clicked(self, button):
        """Show MediaSourceDialog."""
        dialog = MediaSourceDialog(self.controller, self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            selected_values = dialog.get_selected_values()
            print(f"Selected devices: {selected_values}")
        else:
            print("Dialog canceled")

        dialog.destroy()

    def on_play_button_clicked(self, button):
        print("Play Button Clicked!")

    def on_mode_button_clicked(self, button, mode_name):
        """Handle mode button clicks."""
        print(f"{mode_name} Mode Selected!")
        print(f"Panorama button visibility before toggle: {self.panorama_button.get_visible()}")

    # Toggle Panorama button visibility only in Discussion Mode
        if mode_name == "Discussion":
            # Toggle visibility of the Panorama button
            self.panorama_button.set_visible(not self.panorama_button.get_visible())
        else:
            # Hide Panorama button for other modes
            self.panorama_button.set_visible(False)

        print(f"Panorama button visibility after toggle: {self.panorama_button.get_visible()}")
        
    def on_panorama_button_clicked(self, button):
        """Handle Panorama button click."""
        print("Panorama Button Clicked!")

    def on_config_button_clicked(self, button):
        """Toggle the visibility of the sidebar."""
        self.sidebar_revealer.set_reveal_child(not self.sidebar_revealer.get_reveal_child())

    def on_limit_dropdown_changed(self, dropdown):
        """Handle changes in the Limit Person dropdown."""
        selected_value = dropdown.get_active_text()
        if selected_value:
            limit = int(selected_value)
            self.update_view_list(limit)

    def update_view_list(self, limit):
        """Update the view list based on the selected limit."""
        for child in self.view_list_box.get_children():
            self.view_list_box.remove(child)

        for i in range(1, limit + 1):
            view_button = Gtk.Button()
            view_button_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
            view_icon = Gtk.Image.new_from_icon_name("view-app-grid-symbolic", Gtk.IconSize.BUTTON)
            view_label = Gtk.Label(label=f"VIEW {i}")
            view_button_box.pack_start(view_icon, False, False, 0)
            view_button_box.pack_start(view_label, False, False, 0)
            view_button.add(view_button_box)
            view_button.set_size_request(280, 40)
            self.view_list_box.pack_start(view_button, False, False, 0)

        self.sidebar_revealer.set_reveal_child(True)
        self.view_list_box.show_all()

    def on_ai_toggle_button_clicked(self, button):
        """Handle AI toggle button click."""
        if self.ai_toggle_button.get_label() == "AI Tracking (OFF)":
            self.ai_toggle_button.set_label("AI Tracking (ON)")
            self.ai_toggle_button.get_style_context().remove_class("destructive-action")
            self.ai_toggle_button.get_style_context().add_class("suggested-action")  # Green (ON)
        else:
            self.ai_toggle_button.set_label("AI Tracking (OFF)")
            self.ai_toggle_button.get_style_context().remove_class("suggested-action")
            self.ai_toggle_button.get_style_context().add_class("destructive-action")  # Red (OFF)

    def on_panorama_toggle_button_clicked(self, button):
        """Handle AI toggle button click."""
        if  self.panorama_toggle_button.get_label() == "Panorama (OFF)":
            self.panorama_toggle_button.set_label("Panorama(ON)")
            self.panorama_toggle_button.get_style_context().remove_class("destructive-action")
            self.panorama_toggle_button.get_style_context().add_class("suggested-action")  # Green (ON)
        else:
            self.panorama_toggle_button.set_label("Panorama (OFF)")
            self.panorama_toggle_button.get_style_context().remove_class("suggested-action")
            self.panorama_toggle_button.get_style_context().add_class("destructive-action")  # Red (OFF)

    def on_camera_toggle_button_clicked(self, button):
        """Handle Camera toggle button click."""
        if self.camera_toggle_button.get_label() == "Camera Downside":
            self.camera_toggle_button.set_label("Camera Upside")
            self.camera_toggle_button.get_style_context().remove_class("destructive-action")
            self.camera_toggle_button.get_style_context().add_class("suggested-action")  # Green (ON)
        else:
            self.camera_toggle_button.set_label("Camera Downside")
            self.camera_toggle_button.get_style_context().remove_class("suggested-action")
            self.camera_toggle_button.get_style_context().add_class("destructive-action")  # Red (OFF)