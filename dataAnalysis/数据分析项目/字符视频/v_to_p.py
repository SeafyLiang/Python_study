import cv2
import os

# 在当前目录下新建文件夹
folder_path = "img_bear/"
os.makedirs(folder_path)
# 进行视频的载入
vc = cv2.VideoCapture('bear.mp4')
c = 0
# 判断载入的视频是否可以打开
ret = vc.isOpened()
# 循环读取视频帧
while ret:
    c = c + 1
    # 进行单张图片的读取,ret的值为True或者Flase,frame表示读入的图片
    ret, frame = vc.read()
    if ret:
        # 存储为图像
        cv2.imwrite('img_bear/'+str(c) + '.jpg', frame)
        # 输出图像名称
        print('img_bear/'+str(c) + '.jpg')
        # 在一个给定的时间内(单位ms)等待用户按键触发,1ms
        cv2.waitKey(1)
    else:
        break
# 视频释放
vc.release()
