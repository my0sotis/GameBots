# Developed by 刘晓林
import numpy as np
from Cnn_model import alexnet
import warnings
from random import shuffle
import time
warnings.filterwarnings("ignore")

# 屏幕规格
WIDTH = 160
HEIGHT = 40
LR = 1e-3
EPOCHS = 10
MODEL_NAME = 'dinosaur'

# 创建模型
model = alexnet(WIDTH, HEIGHT, LR)
# 加载模型
model.load(MODEL_NAME)

hm_data = 30
for i in range(EPOCHS):
    for i in range(8, hm_data + 1):
        train_data = np.load('training_data-{}.npy'.format(i), allow_pickle=True)

        # 随机打乱数据集
        # shuffle(train_data)

        # 训练集
        train = train_data[:-100]
        # 测试集
        test = train_data[-100:]

        X = np.array([i[0] for i in train]).reshape([-1, WIDTH, HEIGHT, 1])
        Y = [i[1] for i in train]

        test_x = np.array(([i[0] for i in test])).reshape([-1, WIDTH, HEIGHT, 1])
        test_y = [i[1] for i in test]

        # 将数据投喂给神经网络
        model.fit({'input': X}, {'targets': Y}, n_epoch=1, validation_set=({'input': test_x}, {'targets': test_y}),
                  snapshot_step=500, show_metric=True, run_id=MODEL_NAME)

        # 保存模型
        model.save(MODEL_NAME)

#tensorboard --logdir=foo:E:\暑期实训\19暑期实训\项目\newAI\Dinosaur\Dinosaur