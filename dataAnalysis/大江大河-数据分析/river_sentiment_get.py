import urllib.request
import pandas
import json
import time


def get_access_token():
    """
    获取百度AI平台的Access Token
    """
    # 使用你的API Key及Secret Key
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[API Key]&client_secret=[Secret Key]'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    rdata = json.loads(content)
    return rdata['access_token']


def sentiment_classify(text, acc):
    """
    获取文本的感情偏向（消极 or 积极 or 中立）
    参数：
    text:str 本文
    """
    raw = {"text":"内容"}
    raw['text'] = text
    data = json.dumps(raw).encode('utf-8')
    # 情感倾向分析接口
    host = "https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token=" + acc
    request = urllib.request.Request(url=host, data=data)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    rdata = json.loads(content)
    return rdata


# 获取access_token
access_token = get_access_token()
# 差评标签
df = pandas.read_csv('comments_douban_l.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment'])
# 好评标签
# df = pandas.read_csv('comments_douban_a.csv', header=None, names=['user_name', 'user_url', 'registered_time', 'score', 'date', 'comment_time', 'useful_num', 'comment'])

# 输出情感极性分类结果,0:负向,1:中性,2:正向
sentiments = []
for text in df['comment']:
    time.sleep(1)
    result = sentiment_classify(str(text), access_token)
    value = result['items'][0]['sentiment']
    sentiments.append(value)
    # print(result)
    print(result['items'][0]['sentiment'], text)

# 添加评分列及情感列
df['score1'] = df['score']
df['emotional'] = sentiments
# 差评标签
df.to_csv('comments_douban_ll.csv', header=0, index=False, encoding='utf-8-sig')
# 好评标签
# df.to_csv('comments_douban_al.csv', header=0, index=False, encoding='utf-8-sig')
