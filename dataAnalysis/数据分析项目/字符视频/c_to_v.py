import cv2
import os

# 设置视频编码器,这里使用使用MJPG编码器
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# 输出视频参数设置,包含视频文件名、编码器、帧率、视频宽高(此处参数需和字符图片大小一致)
videoWriter = cv2.VideoWriter('bear_character.avi', fourcc, 20.0, (560, 560))

for i in range(1, 1000):
    filename = 'bear/'+str(i)+'.jpg'
    # 判断图片是否存在
    if os.path.exists(filename):
        img = cv2.imread(filename=filename)
        # 在一个给定的时间内(单位ms)等待用户按键触发,100ms
        cv2.waitKey(100)
        # 将图片写入视频中
        videoWriter.write(img)
        print(str(i) + '.jpg' + ' done!')
# 视频释放
videoWriter.release()
