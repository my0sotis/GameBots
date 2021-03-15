import sys
sys.path.append('H:\\OpenAI')

from screenshot import  screenshot
import numpy
import pyautogui
import cv2
from pynput.keyboard import Key, Controller
import gc
from operation import Operation
import win32gui
from PyQt5.QtWidgets import QApplication
import time
from get_key import key_check

# 判断是否退出
isQuit = 0



def chapter1():
   # 声明isQuit为全局变量
   global isQuit

   keyboard = Controller()
   op=Operation()
   app = QApplication(sys.argv)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  # ???????????????Visual Studio??SPY++??????
   for i in range(10000):
      while isQuit == 0:
         start = cv2.getTickCount()

         image = screenshot(hWnd)

         img = numpy.asarray(image)

         if (img[400,0]==numpy.array([254,31,111])).all():
            return

         finalmask = cv2.inRange(img, numpy.array([213, 240, 250]), numpy.array([225, 245, 252]))
         (finalcontours, _) = cv2.findContours(finalmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
         gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)
         gradient = cv2.subtract(gradX, gradY)

         gradient = cv2.convertScaleAbs(gradient)


         playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))
         (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
         playercontours.sort(key=cv2.contourArea, reverse=True)


         if(len(finalcontours)<=0):
            break


         if len(playercontours) > 0:
            cnt = playercontours[0]
            (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)
            keyboard.press(Key.right)

            for i in range(0, int(2 * playerR), 1):
               for j in range(70,90):
                  if (gradient[min(899,int(i + playerY - playerR)), min(1599,int(playerX + playerR + j))] > 0):
                      op.escape()
            del cnt, playerX, playerY, playerR

         del playermask, playercontours,finalcontours,finalmask
         end = cv2.getTickCount()
         # print((end - start) / cv2.getTickFrequency())
         del start, end
         del image, gradient, gradY, gradX,gray,img

         # 点击T退出程序
         keys = key_check()
         if 'T' in keys:
             isQuit = 1
      # 退出for循环
      if isQuit == 1:
         keyboard.release(Key.right)
         return

      keyboard.release(Key.right)


   del hWnd,keyboard,op
   gc.collect()
   sys.exit(app.exec_())


def chapter2():
   op = Operation()
   op.goRight(0.35)
   op.goUp(0.23)
   app = QApplication(sys.argv)
   time.sleep(35)
   hWnd = win32gui.FindWindow(None, "Just Shapes & Beats")  # ???????????????Visual Studio??SPY++??????
   while 1:
      print()
      image = screenshot(hWnd)

      img = numpy.asarray(image)

      playermask = cv2.inRange(img, numpy.array([0, 230, 230]), numpy.array([120, 255, 255]))
      (playercontours, _) = cv2.findContours(playermask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
      playercontours.sort(key=cv2.contourArea, reverse=True)

      if len(playercontours) > 0:
         cnt = playercontours[0]
         (playerX, playerY), playerR = cv2.minEnclosingCircle(cnt)

         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0)
         gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1)
         gradient = cv2.subtract(gradX, gradY)

         gradient = cv2.convertScaleAbs(gradient)


         for i in range(0, int(2 * playerR), 1):
            for j in range(40, 60):
               if (gradient[min(899, int(i + playerY - playerR)), min(1599, int(playerX + playerR + j))] > 0):
                  op.escape()
                  del app, hWnd
                  return

         del playerY, playerX, playerR

      del img, image, playercontours, playermask

def chapter3():
    op =Operation()
    op.goRight(1.2)
    del op


def main():
   chapter1()
   # chapter2()

if __name__ == '__main__':
   main()