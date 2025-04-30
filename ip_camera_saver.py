import cv2
import matplotlib.pyplot as plt
import os

# 저장 경로 설정
save_dir = r"C:\Users\hanta\capstone\version_0.1\train_dataset"
os.makedirs(save_dir, exist_ok=True)  # 폴더가 없으면 자동 생성

import os
import cv2
import matplotlib.pyplot as plt
from config import SAVE_DIR, CAP, NUM_FRAME, FRAME_TIME

class IPCamSaver:
    """
    IP Webcam으로부터 영상을 캡처하여 지정된 폴더에 프레임을 저장

    Attributes:
        cap (cv2.VideoCapture): 비디오 캡처 객체
        save_dir (str): 프레임을 저장할 디렉토리 경로
        num_frame (int): 저장할 프레임 수
        frame_time (float): 프레임 간 표시 시간 (초)
    """
    def __init__(self, cap=CAP, save_dir=SAVE_DIR, num_frame=NUM_FRAME, frame_time=FRAME_TIME):
        self.cap = cap
        self.save_dir = save_dir
        self.num_frame = num_frame
        self.frame_time = frame_time

        os.makedirs(self.save_dir, exist_ok=True)

    def run(self):
        plt.ion()
        frame_count = 0

        while frame_count < self.num_frame:
            ret, frame = self.cap.read()
            if not ret:
                print("프레임을 불러올 수 없습니다.")
                break

            # 실시간 표시
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            plt.imshow(frame_rgb)
            plt.axis('off')
            plt.pause(self.frame_time)
            plt.clf()

            # 프레임 저장
            filename = os.path.join(self.save_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
            frame_count += 1

        self.cap.release()
        plt.close()
