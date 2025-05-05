# config.py

# 저장 폴더 및 스트림 URL
SAVE_DIR      = r"C:\Users\hanta\capstone\version_0.1\train_dataset"
URL           = "http://192.168.119.100:8080/video"
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 캡처 프레임 수, 프레임 표시 시간(초)
NUM_FRAME    = 100
FRAME_TIME   = 0.5

# 이미지 저장 여부 (True: 저장, False: 저장하지 않음)
SAVE_IMAGES  = False

# ── OCR 설정 ────────────────────────────────────────────
# 사용할 언어 코드 (예: 'eng', 'kor', 'eng+kor' 등)
OCR_LANG     = 'kor'
# Tesseract --psm 옵션 (6: 단일 블록, 3: 전체 페이지 등)
OCR_PSM      = 6
# 전처리: True면 그레이스케일→Otsu 이진화 적용
OCR_PREPROCESS = True
