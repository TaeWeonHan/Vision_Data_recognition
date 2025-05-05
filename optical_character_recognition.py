# optical_character_recognition.py

from PIL import Image
import pytesseract
import cv2
import numpy as np
import matplotlib.pyplot as plt
from config import *

# (필요 시) 환경 변수 대신 직접 경로 지정
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

class OCRProcessor:
    """
    프레임(혹은 파일) 단위로
      1) 전처리(그레이스케일+이진화)
      2) OCR 수행
      3) 결과 출력 & 화면 표시
    까지 담당하는 클래스
    """
    def __init__(self, lang: str = OCR_LANG, psm: int = OCR_PSM, preprocess: bool = OCR_PREPROCESS):
        self.lang      = lang
        self.config    = f'--psm {psm}'
        self.preprocess= preprocess

    def _preprocess_frame(self, frame: np.ndarray) -> np.ndarray:
        """
        BGR 프레임 → 그레이 → Otsu 이진화 → RGB 3채널 변환
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(
            gray, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        # 다시 3채널로 만들어 PIL로 변환하기 편하게
        return cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)

    def ocr_image_file(self, path: str) -> str:
        """
        디스크의 이미지 파일에서 OCR 수행
        """
        img = Image.open(path)
        if self.preprocess:
            # PIL → OpenCV → 전처리 → PIL
            npimg = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            proc = self._preprocess_frame(npimg)
            img = Image.fromarray(proc)
        return pytesseract.image_to_string(img, lang=self.lang, config=self.config)

    def ocr_frame(self, frame: np.ndarray) -> str:
        """
        메모리상의 BGR 프레임에서 바로 OCR 수행
        """
        # 전처리 적용
        if self.preprocess:
            proc_rgb = self._preprocess_frame(frame)
            pil_img  = Image.fromarray(proc_rgb)
        else:
            # 단순 BGR→RGB
            pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        return pytesseract.image_to_string(pil_img, lang=self.lang, config=self.config)

    def __call__(self, frame: np.ndarray, idx: int):
        """
        IPCamSaver 의 frame_callback 으로 전달되어 호출됩니다.
        1) OCR 수행
        2) 터미널에 결과 프린트
        3) Matplotlib 으로 화면 출력
        """
        text = self.ocr_frame(frame)
        print(f"\n--- OCR 결과 (frame {idx}) ---")
        print(text.strip() or "[인식된 텍스트 없음]")
        print("-" * 30)

        # 화면에 띄우기 (원본 또는 전처리된 이미지를 보고 싶으면 pil_img 저장 후 display)
        display_img = frame
        plt.imshow(display_img[..., ::-1])  # BGR→RGB
        plt.title(f"Frame {idx}")
        plt.axis('off')
        plt.show(block=False)
        plt.pause(0.001)
        plt.clf()
