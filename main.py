import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\student\\AppData\\Local\\Tesseract-OCR\\tesseract.exe'
gui_on = True#  False


def ocr(img_path):
    # print(pytesseract.image_to_string(Image.open(img_path)))
    img = cv2.imread(img_path)
    black_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    black_img = cv2.adaptiveThreshold(cv2.medianBlur(black_img, 3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
    if gui_on:
        cv2.imshow('image', black_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    pil_image = Image.fromarray(cv2.cvtColor(black_img, cv2.COLOR_BGR2RGB))
    print(pytesseract.image_to_string(pil_image))


def main():
    for img_path in ["01.jpg", "02.jpg", "03.jpg", "04.png", "05.jpg", "06.jpg", "07.jpg"]:
        if gui_on:
            img = cv2.imread(img_path)
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        ocr(img_path)



main()
