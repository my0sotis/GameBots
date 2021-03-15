# 创作者 马如云
from operation import Operation
from PIL import Image

op=Operation()

output = open('data.txt', 'w')
img = Image.open()
img_array = img.load()  # 获取像素点信息
w, h = img.size
for i in range(0, h):
   for j in range(0, w):
      pixel = img_array[j, i]
      print('(', end="", file=output)
      print(j, end="", file=output)
      print(',', end="", file=output)
      print(i, end="", file=output)
      print(')', end=" ", file=output)
      print(pixel, file=output)