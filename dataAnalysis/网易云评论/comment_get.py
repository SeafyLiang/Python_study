import json
import time
import requests

headers = {
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}


def get_comments(page):
    """
        获取评论信息
    """
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_1313354324?limit=20&offset=' + str(page)
    response = requests.get(url=url, headers=headers)
    # 将字符串转为json格式
    result = json.loads(response.text)
    items = result['comments']
    for item in items:

        # 用户名
        user_name = item['user']['nickname'].replace(',', '，')
        # 用户ID
        user_id = str(item['user']['userId'])
        # 获取用户信息
        user_message = get_user(user_id)
        # 用户年龄
        user_age = str(user_message['age'])
        # 用户性别
        user_gender = str(user_message['gender'])
        # 用户所在地区
        user_city = str(user_message['city'])
        # 个人介绍
        user_introduce = user_message['sign'].strip().replace('\n', '').replace(',', '，')
        # 评论内容
        comment = item['content'].strip().replace('\n', '').replace(',', '，')
        # 评论ID
        comment_id = str(item['commentId'])
        # 评论点赞数
        praise = str(item['likedCount'])
        # 评论时间
        date = time.localtime(int(str(item['time'])[:10]))
        date = time.strftime("%Y-%m-%d %H:%M:%S", date)
        print(user_name, user_id, user_age, user_gender, user_city, user_introduce, comment, comment_id, praise, date)

        with open('music_comments.csv', 'a', encoding='utf-8-sig') as f:
            f.write(user_name + ',' + user_id + ',' + user_age + ',' + user_gender + ',' + user_city + ',' + user_introduce + ',' + comment + ',' + comment_id + ',' + praise + ',' + date + '\n')
        f.close()


def get_user(user_id):
    """
    获取用户注册时间
    """
    data = {}
    url = 'https://music.163.com/api/v1/user/detail/' + str(user_id)
    # 使用2808proxy代理
    response = requests.get(url=url, headers=headers)
    # 将字符串转为json格式
    js = json.loads(response.text)
    if js['code'] == 200:
        # 性别
        data['gender'] = js['profile']['gender']
        # 年龄
        if int(js['profile']['birthday']) < 0:
            data['age'] = 0
        else:
            data['age'] = (2018 - 1970) - (int(js['profile']['birthday']) // (1000 * 365 * 24 * 3600))
        if int(data['age']) < 0:
            data['age'] = 0
        # 城市
        data['city'] = js['profile']['city']
        # 个人介绍
        data['sign'] = js['profile']['signature']
    else:
        data['gender'] = '无'
        data['age'] = '无'
        data['city'] = '无'
        data['sign'] = '无'
    return data


def main():
    for i in range(0, 25000, 20):
        print('\n---------------第 ' + str(i // 20 + 1) + ' 页---------------')
        get_comments(i)


if __name__ == '__main__':
    main()
