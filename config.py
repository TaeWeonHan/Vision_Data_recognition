import cv2

# cam save dir
SAVE_DIR = r"C:\Users\hanta\capstone\version_0.1\train_dataset"

# web cam URL
URL = "http://192.168.119.100:8080/video"
CAP = cv2.VideoCapture(URL)

# runtime settings
NUM_FRAME = 30
FRAME_TIME = 0.5