from PIL import Image
import cv2
import numpy as np
from flask_cors import CORS
from flask import Flask, request, json
import base64

app = Flask(__name__)


def base64_to_array(base64_string):
    nparr = np.fromstring(base64.b64decode(base64_string), np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


@app.route("/",  methods=['POST'])
def hello():
    image = base64_to_array(request.form['File'])
    cv2.imwrite("hinh.png", image)
    return "image"


@app.route("/",  methods=['GET'])
def hello1():
    return "oke"


if __name__ == "__main__":
    app.run()
CORS(app)
