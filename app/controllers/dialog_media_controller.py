class MediaDialogController:
    def __init__(self, model):
        self.model = model
        self.selected_device_index = None

    def get_available_cameras(self):
        """Get the list of available cameras from the model."""
        self.model.detect_cameras()
        return [(index, name) for index, name in self.model.available_cameras]

    def get_camera_names(self):
        """Get the list of camera names from the model."""
        return self.model.get_camera_names()

    def set_selected_values(self, device_index):
        """Set selected values from dialog."""
        self.selected_device_index = device_index
