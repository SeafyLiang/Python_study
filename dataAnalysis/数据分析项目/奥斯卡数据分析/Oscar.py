import time
import requests
from bs4 import BeautifulSoup

filenames = ['Best_Actor_LR.csv', 'Best_Actress_LR.csv', 'Best_Actor_SR.csv', 'Best_Actress_SR.csv']


def get_message(num1, num2):
    """获取数据"""
    time.sleep(5)
    years, wins, nominations = [[], [], []]
    # 请求网址
    url = 'http://award.mtime.com/3/award/3' + str(num1) + '/index' + str(num2) + '.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    html = response.text
    # 对请求结果进行编码解码处理,避免出现乱码
    html = html.encode('ISO-8859-1')
    html = html.decode('utf-8')
    # 提取信息
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all(class_='event_awards event_list')
    # 获取时间信息
    for dt in div[0].find_all('dt'):
        if len(dt) == 1:
            year = dt.get_text().replace('\n', '').strip()
            years.append(year)
    # 获取获奖者信息
    for dd in soup.find_all(class_='yellowbox'):
        win = dd.find(class_='px14 c_a5').find('a').get_text().split(' ')[0]
        wins.append(win)
    # 获取提名者信息
    for dd in soup.find_all(class_='bluebox'):
        names = []
        for k in dd.find_all(class_='px14 c_a5'):
            name = k.get_text().strip().split(' ')[0]
            names.append(name)
        # 提名者有多个,拼接提名者信息
        nomination = ' '.join(names)
        nominations.append(nomination)
    # 写入CSV文件中
    for year, win, nomination in zip(years, wins, nominations):
        print(year, win, nomination)
        filename = filenames[num1]
        with open(filename, 'a+') as f:
            f.write(year + ',' + win + ',' + nomination + '\n')
        f.close()


if __name__ == '__main__':
    for i in range(4):
        num1 = i
        for j in range(1, 10):
            if j == 1:
                num2 = ''
            else:
                num2 = -j
            get_message(num1, num2)
