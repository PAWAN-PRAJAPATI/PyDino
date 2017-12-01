import numpy as np
from alexnet import alexnet
import cv2
import time
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import os
import pyautogui
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'pygta5-car-fast-{}-{}-{}-epochs-300K-data.model'.format(LR, 'alexnetv2',EPOCHS)

t_time = 0.09

model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)
def grab():
    img = ImageGrab.grab(bbox=(10, 190, 600, 310))  # x, y, w, h
    img_np = np.array(img)
    return img_np

while (True):
        # 800x600 windowed mode
        # screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        screen = grab()
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (160, 120))
        prediction = model.predict([screen.reshape(160, 120, 1)])[0]
        if(float(prediction[0])>0.40 ):
            pyautogui.press(" ")



