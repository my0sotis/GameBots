# 创作者 马如云
import sys
sys.path.append('H:\\OpenAI')

from screenshot import  screenshot
import numpy
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
from numba import jit
import gc
from operation import Operation
from cProfile import Profile
import win32gui
from PyQt5.QtWidgets import QApplication
import math
from point import Point
import time

def main():
   keyboard = Controller()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")
   for i in range(10000):
      while 1:
         start = cv2.getTickCount()

         image = screenshot(hWnd)

         img = numpy.asarray(image)
         print(img[0, 0])
         # if (img[0,0]==numpy.array([2,27,35])).all() or (img[0,0]==numpy.array([21,36,37])).all():
         #    print(1)
         #    return
         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)
         if len(playercontours)<=0:
            return

         if len(playercontours) > 0:
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)

            for i in range(0, 60):
                  if ((img[int(playerY+i), int(playerX + playerR+40)]==numpy.array([0,0,0])).all()==False):
                     keyboard.press(Key.up)
                     time.sleep(0.01*i/20)
                     keyboard.release(Key.up)
                     break
                  if ((img[int(playerY-i), int(playerX + playerR+40)]==numpy.array([0,0,0])).all()==False):
                     keyboard.press(Key.down)
                     time.sleep(0.01*i/20)
                     keyboard.release(Key.down)
                     break

         end = cv2.getTickCount()
         print((end - start) / cv2.getTickFrequency())

   del hWnd,keyboard
   gc.collect()
   sys.exit(app.exec_())

def main2():
   keyboard = Controller()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")
   for i in range(10000):
      while 1:
         start = cv2.getTickCount()

         image = screenshot(hWnd)

         img = numpy.asarray(image)

         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)

         if len(playercontours) > 0:
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)


            for i in range(0, 60):
               if ((img[int(playerY  +i), int(playerX + playerR+20)] == numpy.array([0, 0, 0])).all() == False):

                  keyboard.press(Key.up)
                  time.sleep(0.01*i/10)
                  keyboard.release(Key.up)
                  break
               if ((img[int(playerY - i), int(playerX + playerR+20)] == numpy.array([0, 0, 0])).all() == False):
                  keyboard.press(Key.down)
                  time.sleep(0.01*i/10)
                  keyboard.release(Key.down)
                  break



         end = cv2.getTickCount()
         print((end - start) / cv2.getTickFrequency())

   del hWnd, keyboard
   gc.collect()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()
   main2()