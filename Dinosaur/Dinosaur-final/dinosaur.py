# create by 高战立
import numpy as np
from grabscreen import grab_screen, process_img
import cv2
import pyautogui
import time
from get_key import key_check

# 显示截图图片，主要功能是用于调试
def show_img():

    while (True):
        # 按区域获取屏幕截图
        img = grab_screen(region=(560, 147, 1360, 347))
        img = np.array(img)
        # 显示图片
        cv2.imshow('dinosaur', img)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destoryAllWindows()
            break

# 小恐龙向上跳的函数
def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.12)
    # 点击下操作是防止小恐龙悬空期间再次点击space无反应的问题
    pyautogui.press('down')
    pyautogui.keyUp('space')


# 通过图像识别实现小恐龙游戏AI
def process_item():
    paused = False
    while True:
        img = grab_screen(region=(560, 147, 1360, 347))
        # 转换为像素数组
        img_array = img.load()

        num = 0
        # 100 和 110 为小恐龙坐标值
        # 通过小恐龙前方障碍物像素点数进行判断，若达到一定数量则起跳
        for d_x in range(100 + 45, 100 + 95):
            for d_y in range(110,110 + 60):
                pixel = img_array[d_x,d_y]
                if pixel == (83, 83, 83) or pixel == (172, 172, 172):
                    num = num + 1
        # 大于93起跳，躲避障碍物
        if num > 93:
            pressSpace()

        print(num)
        # 键盘输入
        keys = key_check()

        # 实现点击T暂停一段时间的功能
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused !')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(4)
show_img()
# process_item()