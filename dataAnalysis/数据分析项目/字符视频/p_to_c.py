from PIL import Image, ImageDraw, ImageFont
import numpy as np
import os

# 创建字符图片文件夹
folder_path = "bear/"
os.makedirs(folder_path)
for i in range(1, 1000):
    filename = 'img_bear/' + str(i) + '.jpg'
    # 字符列表
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~            <>i!lI;:,\"^`'. ")
    # 判断图片是否存在
    if os.path.exists(filename):
        # 将图片转化为灰度图像,并重设大小
        img_array = np.array(Image.open(filename).resize((70, 70), Image.ANTIALIAS).convert('L'))
        # 创建新的图片对象
        img = Image.new('L', (560, 560), 255)
        draw_object = ImageDraw.Draw(img)
        # 设置字体
        font = ImageFont.truetype('consola.ttf', 10, encoding='unic')
        # 根据灰度值添加对应的字符
        for j in range(70):
            for k in range(70):
                x, y = k * 8, j * 8
                index = int(img_array[j][k] / 4)
                draw_object.text((x, y), ascii_char[index], font=font, fill=0)
        name = 'bear/' + str(i) + '.jpg'
        print(name)
        # 保存字符图片
        img.save(name, 'JPEG')