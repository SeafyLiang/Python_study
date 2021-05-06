import time
import requests
import proxy2808
from bs4 import BeautifulSoup

USERNAME = '用户名'
PASSWORD = '密码'

headers = {
    'Cookie': '你的Cookie值',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_comments(page, proxy_url_secured):
    """
    评论获取
    """
    # 热门评论获取
    url = 'https://movie.douban.com/subject/26797690/comments?start=' + str(page) + '&limit=20&sort=new_score&status=P'
    # 好评获取
    # url = 'https://movie.douban.com/subject/26797690/comments?start=' + str(page) + '&limit=20&sort=new_score&status=P&percent_type=h'
    # 一般评论获取
    # url = 'https://movie.douban.com/subject/26797690/comments?start=' + str(page) + '&limit=20&sort=new_score&status=P&percent_type=m'
    # 差评获取
    # url = 'https://movie.douban.com/subject/26797690/comments?start=' + str(page) + '&limit=20&sort=new_score&status=P&percent_type=l'
    # 使用2808proxy代理
    response = requests.get(url=url, headers=headers, proxies={'http': proxy_url_secured, 'https': proxy_url_secured})
    soup = BeautifulSoup(response.text, 'html.parser')
    for div in soup.find_all(class_='comment-item'):
        time.sleep(3)
        # 评论信息
        comment_info = div.find(class_='comment-info')
        # 用户名
        user_name = comment_info.find('a').get_text()
        print(user_name)
        # 用户主页地址
        user_url = comment_info.find('a').attrs['href']
        print(user_url)
        # 获取用户注册时间,看水军必备
        registered_time = get_user(user_url, proxy_url_secured)
        print(registered_time)
        # 用户评分
        score = comment_info.find_all('span')[1].attrs['class'][0][-2:-1]
        print(score)
        # 用户评价
        eva = comment_info.find_all('span')[1].attrs['title']
        print(eva)
        # 有用数
        useful_num = div.find(class_='votes').get_text()
        print(useful_num)
        # 评价日期
        date = comment_info.find(class_='comment-time ').attrs['title'].split(' ')[0]
        print(date)
        # 评价时间
        comment_time = comment_info.find(class_='comment-time ').attrs['title'].split(' ')[1]
        print(comment_time)
        # 用户评论
        comment = div.find(class_='short').get_text().replace('\n', '').strip().replace(',', '，').replace(' ', '')
        print(comment)
        # 写入csv文件
        with open('comments_douban_l.csv', 'a', encoding='utf-8-sig') as f:
            f.write(user_name + ',' + user_url + ',' + registered_time + ',' + score + ',' + date + ',' + comment_time + ',' + useful_num + ',' + comment + '\n')
        f.close()


def get_user(user_url, proxy_url_secured):
    """
    获取用户注册时间
    """
    # 使用2808proxy代理
    response = requests.get(url=user_url, headers=headers, proxies={'http': proxy_url_secured, 'https': proxy_url_secured})
    soup = BeautifulSoup(response.text, 'html.parser')
    user_message = soup.find(class_='basic-info')
    # 获取用户注册时间
    try:
        user_registered = user_message.find(class_='pl')
        registered_time = user_registered.get_text().split('  ')[1].replace('加入', '')
    except:
        registered_time = 'unknow'
    return registered_time


def main():
    num = 0
    for i in range(0, 500, 20):
        cli = proxy2808.Client(username=USERNAME, password=PASSWORD)
        cli.release_all()
        p = cli.get_proxies(amount=1, expire_seconds=300)[0]
        proxy_url_secured = "%s://%s:%s@%s:%d" % ('http', USERNAME, PASSWORD, p['ip'], p['http_port_secured'])
        print(proxy_url_secured)
        get_comments(i, proxy_url_secured)
        num += 1


if __name__ == '__main__':
    main()
