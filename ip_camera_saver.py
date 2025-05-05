# ip_camera_saver.py

import os
import cv2
import matplotlib.pyplot as plt
from config import SAVE_DIR, URL, NUM_FRAME, FRAME_TIME, SAVE_IMAGES

class IPCamSaver:
    def __init__(self,
                 save_dir: str = SAVE_DIR,
                 url: str = URL,
                 num_frame: int = NUM_FRAME,
                 frame_time: float = FRAME_TIME,
                 save_images: bool = SAVE_IMAGES,
                 frame_callback=None):
        """
        :param save_images: config.SAVE_IMAGES 에 따라 디스크 저장 여부를 결정
        :param frame_callback: frame_callback(frame: np.ndarray, idx: int)
        """
        self.save_dir       = save_dir
        os.makedirs(self.save_dir, exist_ok=True)

        self.url            = url
        self.cap            = cv2.VideoCapture(self.url)
        self.num_frame      = num_frame
        self.frame_time     = frame_time
        self.save_images    = save_images
        self.frame_callback = frame_callback

    def run(self):
        plt.ion()
        for i in range(self.num_frame):
            ret, frame = self.cap.read()
            if not ret:
                print("프레임을 가져올 수 없습니다.")
                break

            # (1) 디스크에 저장 (config.SAVE_IMAGES)
            if self.save_images:
                fname = os.path.join(self.save_dir, f"frame_{i:04d}.jpg")
                cv2.imwrite(fname, frame)

            # (2) callback 호출
            if self.frame_callback:
                self.frame_callback(frame, i)

            # (3) 실시간 표시 (필요 없으면 주석 처리)
            plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            plt.axis('off')
            plt.pause(self.frame_time)
            plt.clf()

        self.cap.release()
        plt.close()
