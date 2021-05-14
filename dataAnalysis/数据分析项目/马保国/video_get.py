from bilibili_api import video, Verify
import requests
import urllib3

# 参数
verify = Verify("你的SESSDATA值", "你的bili_jct值")

# 获取下载地址
download_url = video.get_download_url(bvid="BV1JV41117hq", verify=verify)
print(download_url["dash"]["video"][0]['baseUrl'])

baseurl = 'https://www.bilibili.com/video/BV1JV41117hq'
title = '马保国'


def get_video():
    urllib3.disable_warnings()

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
    }
    headers.update({'Referer': baseurl})
    res = requests.Session()
    begin = 0
    end = 1024 * 1024 - 1
    flag = 0

    temp = download_url

    filename = "./" + title + ".flv"
    url = temp["dash"]["video"][0]['baseUrl']
    while True:
        headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
        res = requests.get(url=url, headers=headers, verify=False)
        if res.status_code != 416:
            begin = end + 1
            end = end + 1024 * 1024
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = requests.get(url=url, headers=headers, verify=False)
            flag = 1
        with open(filename, 'ab') as fp:
            fp.write(res.content)
            fp.flush()
        if flag == 1:
            fp.close()
            break

    print('--------------------------------------------')
    print('视频下载完成')
    filename = "./" + title + ".mp3"
    url = temp["dash"]["audio"][0]['baseUrl']
    while True:
        headers.update({'Range': 'bytes=' + str(begin) + '-' + str(end)})
        res = requests.get(url=url, headers=headers, verify=False)
        if res.status_code != 416:
            begin = end + 1
            end = end + 1024 * 1024
        else:
            headers.update({'Range': str(end + 1) + '-'})
            res = requests.get(url=url, headers=headers, verify=False)
            flag = 1
        with open(filename, 'ab') as fp:
            fp.write(res.content)
            fp.flush()
        if flag == 1:
            fp.close()
            break

    print('音频下载完成')


get_video()