import re
import os
import cv2
import jieba
import stylecloud


def get_text_content(text_file_path):
    '''
    获取填充文本内容
    '''
    text_content = ''
    with open(text_file_path, encoding='utf-8') as file:
        text_content = file.read()
    # 数据清洗，只保存字符串中的中文，字母，数字
    text_content_find = re.findall('[\u4e00-\u9fa5a-zA-Z0-9]+', text_content, re.S)
    text_content = ' '.join(jieba.cut(str(text_content_find).replace(" ", ""), cut_all=False))
    print(text_content)
    return text_content


text_content = get_text_content('danmu.txt')


def transform_video_to_image(video_file_path, img_path):
    '''
    将视频中每一帧保存成图片
    '''
    video_capture = cv2.VideoCapture(video_file_path)
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    count = 0
    while (True):
        ret, frame = video_capture.read()
        if ret:
            cv2.imwrite(img_path + '%d.jpg' % count, frame)
            count += 1
        else:
            break
    video_capture.release()

    filename_list = os.listdir(img_path)
    with open(os.path.join(img_path, 'img_list.txt'), 'w', encoding='utf-8') as file:
        file.writelines('\n'.join(filename_list))

    print('视频图片保存成功, 共有 %d 张' % count)
    return fps


input_video = 'work/videos/Master_Ma.mp4'
fps = transform_video_to_image(input_video, 'work/mp4_img/')


def create_wordcloud():
    for i in range(1, 565):
        file_name = os.path.join("mp4_img_mask/", str(i) + '.png')
        # print(file_name)
        result = os.path.join("work/mp4_img_analysis/", 'result' + str(i) + '.png')
        # print(result)
        stylecloud.gen_stylecloud(text=text_content,
                                  font_path='方正兰亭刊黑.TTF',
                                  output_name=result,
                                  background_color="black",
                                  mask_img=file_name)


create_wordcloud()


def combine_image_to_video(comb_path, output_file_path, fps=30, is_print=False):
    '''
    合并图像到视频
    '''
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    file_items = [item for item in os.listdir(comb_path) if item.endswith('.png')]
    file_len = len(file_items)
    # print(comb_path, file_items)
    if file_len > 0:
        print(file_len)
        temp_img = cv2.imread(os.path.join(comb_path, file_items[0]))
        img_height, img_width, _ = temp_img.shape

        out = cv2.VideoWriter(output_file_path, fourcc, fps, (img_width, img_height))

        for i in range(file_len):
            pic_name = os.path.join(comb_path, 'result' + str(i) + ".png")
            print(pic_name)
            if is_print:
                print(i + 1, '/', file_len, ' ', pic_name)
            img = cv2.imread(pic_name)
            out.write(img)
        out.release()


combine_image_to_video('work/mp4_img_analysis/', 'work/mp4_analysis.mp4', 30)


# 灰度图
img = cv2.imread('work/mp4_img_mask/240.png', 0)
# 二值化
ret, thresh = cv2.threshold(img, 30, 255, cv2.THRESH_BINARY_INV)
# 显示
cv2.imshow("img", thresh)
# 保存图片
cv2.imwrite('0.png', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
