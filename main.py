# main.py

from ip_camera_saver import IPCamSaver
from optical_character_recognition import OCRProcessor
from config import NUM_FRAME, FRAME_TIME  # SAVE_IMAGES 등은 ip_camera_saver.py에서 직접 읽어옵니다

def main():
    # 1) OCRProcessor 객체 생성
    ocr_processor = OCRProcessor(lang='eng', psm=6)

    # 2) IPCamSaver 에 callback 으로 전달
    saver = IPCamSaver(
        num_frame=NUM_FRAME,
        frame_time=FRAME_TIME,
        frame_callback=ocr_processor
    )

    # 3) 실행
    saver.run()

if __name__ == "__main__":
    main()
