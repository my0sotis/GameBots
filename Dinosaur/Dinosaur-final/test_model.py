# update by 高战立
from old_grab import grab_screen
from Cnn_model import alexnet
import pyautogui
import time
import cv2
from get_key import key_check
from selenium import webdriver
import os

# 缩放的宽度和高度
WIDTH = 160
HEIGHT = 40
LR = 1e-3

# 模型名字
MODEL_NAME = 'dinosaur'
model = alexnet(WIDTH, HEIGHT, LR)
model.load(MODEL_NAME)


# 判断是否退出
isQuit = False

# 扫描函数，进行预测
def scan():
    global isQuit
    last_time = time.time()
    screen = grab_screen(region=(560, 147, 1360, 347))

    # 输出截取事件间隔
    print('loop took {} secon ds'.format(time.time() - last_time))
    last_time = time.time()
    # 二值化
    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # 重塑大小
    screen = cv2.resize(screen, (WIDTH, HEIGHT))

    # 根据模型进行预测
    prediction = model.predict([screen.reshape(WIDTH, HEIGHT, 1)])[0]

    print(prediction)

    # 跳的概率大于0.3时执行动作
    if prediction[0] > 0.3:
        pyautogui.keyDown('space')
        time.sleep(0.13)
        pyautogui.press('down')
        pyautogui.keyUp('space')

    keys = key_check()

    # 输入T退出程序
    if 'T' in keys:
        isQuit = True


# 倒计时
def start():
    for i in list(range(5))[::-1]:
        print(i + 1)
        time.sleep(1)


if __name__ == "__main__":
    # 自动控制浏览器打开网页版小恐龙游戏
    driver = webdriver.Chrome("..\\chromedriver.exe")
    local_path = os.path.abspath("..")
    html_path = 'file://' + local_path + '/Dinosaur-map/index.html '
    driver.maximize_window()
    driver.get(html_path)

    start()
    # 初始加载点击space开始游戏
    pyautogui.press('space')
    while True:
        scan()
        # 输入T时退出程序
        if isQuit == True:
            driver.quit()
            break
