import cv2 as cv
import os

cvNet = cv.dnn.readNetFromTensorflow('MobileNet-SSD v1\\frozen_inference_graph.pb', 'MobileNet-SSD v1\\frozen_inference_graph.pbtxt')

for file_img in os.listdir("data"):
    print(file_img)
    img = cv.imread("data\\"+file_img)
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()

    for detection in cvOut[0,0,:,:]:
        print(dir(detection))
        score = float(detection[2])
        if score > 0.4:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 10), thickness=2)
        elif score > 0.25:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (123, 230, 210), thickness=2)
        elif score > 0.2:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (223, 30, 210), thickness=2)

    cv.imshow('img', img)
    cv.waitKey()