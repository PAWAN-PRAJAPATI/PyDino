
from __future__ import print_function
import pyxhook
import time
import cv2
import pyscreenshot as ImageGrab
import numpy as np
import os
from random import shuffle

def grab():
    img = ImageGrab.grab(bbox=(10, 190, 600, 310))  # x, y, w, h
    img_np = np.array(img)
    return img_np


def kbevent(event):
    global running
    if event.Ascii == 32:
        running = False

hookman = pyxhook.HookManager()
hookman.KeyDown = kbevent
hookman.HookKeyboard()
hookman.start()
running = True

file_new = 'balanced_data_2.npy'
file_name ='training_data_2.npy'
if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exist, starting fresh!')
    training_data = []
def read():
    shuffle(training_data)
    final_data = list(np.load(file_new))
    shuffle(final_data)
    jump=[]
    non_jump=[]
    print(len(training_data))
    for data in training_data:
        if(data[1]==[1,0]):
            jump.append(data)
        elif(data[1]==[0,1]):
            non_jump.append(data)
    non_jump=non_jump[:len(jump)]
    final=jump + non_jump+final_data
    shuffle(final)
    shuffle(final)
    np.save(file_new, final)

    for data in final:
        print(data[1])
        cv2.imshow('Test',data[0])
        cv2.waitKey(20)
    print(len(final))
    #cv2.imshow('test',training_data[0])
def main():
    global running
    while True:
        screen = grab()
        screen =cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen, (160, 120))
        cv2.imshow('Test',screen)
        if(running==False):
            output=[1,0]
            running = True
        else:
            output = [0,1]
        training_data.append([screen,output])
        if len(training_data) % 100 == 0:
            print(len(training_data))
            np.save(file_name, training_data)
        cv2.waitKey(1)

read()
hookman.cancel()
