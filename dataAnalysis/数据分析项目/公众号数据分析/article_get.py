import requests
import json
import time


def parse(__biz, uin, key, pass_ticket, appmsg_token="", offset="0"):
    """
    文章信息获取
    """
    url = '?txe_eliforp/pm/moc.qq.nixiew.pm//:sptth'[::-1]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 QQBrowser/9.0.2524.400",
    }
    params = {
        "action": "getmsg",
        "__biz": __biz,
        "f": "json",
        "offset": str(offset),
        "count": "10",
        "is_ok": "1",
        "scene": "124",
        "uin": uin,
        "key": key,
        "pass_ticket": pass_ticket,
        "wxtoken": "",
        "appmsg_token": appmsg_token,
        "x5": "0",
    }

    res = requests.get(url, headers=headers, params=params, timeout=3)
    data = json.loads(res.text)
    # 获取信息列表
    msg_list = eval(data.get("general_msg_list")).get("list", [])
    for i in msg_list:
        # 去除文字链接
        try:
            # 文章标题
            title = i["app_msg_ext_info"]["title"].replace(',', '，')
            # 文章摘要
            digest = i["app_msg_ext_info"]["digest"].replace(',', '，')
            # 文章链接
            url = i["app_msg_ext_info"]["content_url"].replace("\\", "").replace("http", "https")
            # 文章发布时间
            date = i["comm_msg_info"]["datetime"]
            print(title, digest, url, date)
            with open('article_caojiang5.csv', 'a') as f:
                f.write(title + ',' + digest + ',' + url + ',' + str(date) + '\n')
        except:
            pass
    # 判断是否可继续翻页 1-可以翻页  0-到底了
    if 1 == data.get("can_msg_continue", 0):
        time.sleep(3)
        parse(__biz, uin, key, pass_ticket, appmsg_token, data["next_offset"])
    else:
        print("爬取完毕")


if __name__ == '__main__':
    # 请求参数
    __biz = '你的参数'
    uin = '你的参数'
    key = '你的参数'
    pass_ticket = '你的参数'
    # 解析函数
    parse(__biz, uin, key, pass_ticket, appmsg_token="", offset="0")