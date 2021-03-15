# 利用alexnet模型
# use by alphabeats
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
from tflearn.layers.normalization import local_response_normalization

def alexnet(width, height, lr):

    # 模型输入：截图和键盘操作
    network = input_data(shape=[None, width, height, 1], name='input')
    # 卷积层
    network = conv_2d(network, 96, 11, strides=4, activation='relu')
    # 池化层
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 256, 5, activation='relu')     # 卷积层
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    network = conv_2d(network, 384, 3, activation='relu')     # 卷积层
    network = conv_2d(network, 384, 3, activation='relu')     # 卷积层
    network = conv_2d(network, 256, 3, activation='relu')     # 卷积层
    network = max_pool_2d(network, 3, strides=2)
    network = local_response_normalization(network)
    # 全连接层
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 4096, activation='tanh')
    network = dropout(network, 0.5)
    network = fully_connected(network, 2, activation='softmax')
    network = regression(network, optimizer='momentum',
                         loss='categorical_crossentropy',
                         learning_rate=lr, name='targets')

    model = tflearn.DNN(network, checkpoint_path='model_alexnet',
                        max_checkpoints=1, tensorboard_verbose=2, tensorboard_dir='log')

    return model