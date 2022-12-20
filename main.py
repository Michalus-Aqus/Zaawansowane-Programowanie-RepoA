# Use "python -m flask run" to run server
from flask import Flask, request
import cv2
from PIL import Image
import numpy as np


home="/config_this_path/"

app = Flask(__name__)

cvNet = cv.dnn.readNetFromTensorflow(home+'MobileNet-SSD v1\\frozen_inference_graph.pb', home+'MobileNet-SSD v1\\frozen_inference_graph.pbtxt')

def person_decetion(img):
    res=[]
    cv=cv2
    rows = img.shape[0]
    cols = img.shape[1]
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), swapRB=True, crop=False))
    cvOut = cvNet.forward()
    for detection in cvOut[0, 0, :, :]:
        score = float(detection[2])
        if detection[1] == 1:  # person
            if score > 0.25:
                res.append({
                    "left": detection[3]*cols,
                    "top": detection[4] * rows,
                    "right": detection[5] * cols,
                    "bottom": detection[6] * rows,
                })
    return res


@app.route("/new_app2/", methods = ['POST'])
def new_app_post():
    # just stupid converting
    image_file = request.files['image']
    pil_image=Image.open(image_file)
    cv_imgage = np.asarray(pil_image)
    # fun
    img=cv_imgage
    return str(person_decetion(img))
