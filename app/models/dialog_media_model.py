import os
import cv2
from pygrabber.dshow_graph import FilterGraph


class DialogMediaModel:
    def __init__(self):
        self.path_file = os.path.dirname(os.path.realpath(__file__))
        self.available_cameras = []  # To store detected cameras
        self.detect_cameras()  # Detect cameras during initialization

    def detect_cameras(self):
        """Detect available cameras on the system and their indices."""
        graph = FilterGraph()
        camera_list = graph.get_input_devices()  # Get camera names from pygrabber

        self.available_cameras = []
        for index, camera_name in enumerate(camera_list):
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)  # Use DirectShow as the backend
            if cap.isOpened():  # Check if the camera is valid
                ret, _ = cap.read()  # Attempt to read a frame
                if ret:  # Camera is valid if a frame is successfully read
                    self.available_cameras.append((index, camera_name))
                else:
                    print(f"Invalid camera detected at index {index} ({camera_name})")
                cap.release()
            else:
                print(f"Failed to open camera at index {index} ({camera_name})")