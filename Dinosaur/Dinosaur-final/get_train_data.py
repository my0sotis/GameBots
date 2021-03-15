# Developed by 刘晓林
# update by 高战立
import numpy as np
from old_grab import grab_screen
import cv2
import time
from get_key import key_check
import os

starting_value = 1

# 存储输入的操作，output[0] = 1代表执行跳的操作
def keys_to_output(keys):
    output = [0,0]
    if 'space' in keys:
        output[0] = 1
    else:
        output[1] = 1
    return output


def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []

    # 开始倒计时
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()
    paused = False
    print('STARTING!!!')

    while True:
        if not paused:
            now = time.time()
            # 获取屏幕截图
            screen = grab_screen(region=(560, 147, 1360, 347))
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # resize减小大小
            screen = cv2.resize(screen, (160, 40))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen, output])
            print(time.time() - now)

            if len(training_data) % 100 == 0:
                print(len(training_data))

                if len(training_data) == 500:
                    np.save(file_name, training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'training_data-{}.npy'.format(starting_value)

        keys = key_check()

        # 输入T实现暂停功能
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(4)

def record():
    main(file_name, starting_value)

if __name__ == '__main__':
    while True:
        file_name = 'training_data-{}.npy'.format(starting_value)

        if os.path.isfile(file_name):
            print('File exists, moving along', starting_value)
            starting_value += 1
        else:
            print('File does not exist, starting fresh!', starting_value)
            break
    record()
