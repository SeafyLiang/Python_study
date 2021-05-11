#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   music163.py    
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2021/5/11 08:48   SeafyLiang   1.0     爬取网易云榜单音乐
"""
import requests
from lxml import etree
import os
import time

# 若需下载更多音乐，需登录，在hd中传入cookie
url = 'https://music.163.com/discover/toplist'
hd = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}


def get_topic_ids():
    r = requests.get(url, headers=hd)
    html = etree.HTML(r.text)
    nodes = html.xpath("//ul[@class='f-cb']/li")
    print('{}  {}'.format('榜单 ID', '榜单名称'))
    ans = dict()
    for node in nodes:
        id = node.xpath('./@data-res-id')[0]
        name = node.xpath("./div/p[@class='name']/a/text()")[0]
        ans[id] = name
        print('{}  {}'.format(id, name))
    return ans


def get_topic_songs(topic_id, topic_name):
    params = {
        'id': topic_id
    }
    r = requests.get(url, params=params, headers=hd)
    html = etree.HTML(r.text)
    nodes = html.xpath("//ul[@class='f-hide']/li")
    ans = dict()
    print('{} 榜单 {} 共有歌曲 {} 首 {}'.format('*' * 10, topic_name, len(nodes), '*' * 10))
    for node in nodes:
        id = node.xpath('./a/@href')[0].split('=')[1]
        name = node.xpath('./a/text()')[0]
        ans[id] = name
        print('{}  {}'.format(id, name))

    return ans


def down_song_by_song_id_name(id, name, download_dir):
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
    r = requests.get(url.format(id), headers=hd)
    is_fail = False
    try:
        with open(download_dir + name + '.mp3', 'wb') as f:
            f.write(r.content)
    except:
        is_fail = True
        print("%s 下载出错" % name)
    if (not is_fail):
        print("%s 下载完成" % name)


def down_song_by_topic_id(topicId, topicName):
    download_dir = './data/%s' % topicName + '/'
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    topicMusicList = get_topic_songs(topicId, topicName)
    for id in topicMusicList:
        name = topicMusicList[id]
        down_song_by_topic_id(id, name)
        url = 'http://music.163.com/song/media/outer/url?id={}.mp3'
        r = requests.get(url.format(id), headers=hd)
        is_fail = False
        try:
            with open(download_dir + name + '.mp3', 'wb') as f:
                f.write(r.content)
        except:
            is_fail = True
            print("%s 下载出错" % name)
        if not is_fail:
            print("%s 下载完成" % name)


def main():
    ids = get_topic_ids()
    while True:
        print('')
        print('输入 Q 退出程序')
        print('输入 A 下载全部榜单歌曲')
        print('输入榜单 Id 下载当前榜单歌曲')

        id = input('请输入：')

        if str(id) == 'Q':
            break
        elif str(id) == 'A':
            for id in ids:
                down_song_by_topic_id(id, ids[id])
        else:
            print('')
            ans = get_topic_songs(id, ids[id])
            topicName = ids[id]
            print('')
            print('输入 Q 退出程序')
            print('输入 A 下载全部歌曲')
            print('输入歌曲 Id 下载当前歌曲')
            id = input('请输入：')
            if str(id) == 'Q':
                break
            elif id == 'A':
                for musicId in ans:
                    down_song_by_song_id_name(musicId, ans[musicId], './data/%s-%s/' % (
                        topicName, time.strftime("%Y-%m-%d", time.localtime())))
            else:
                down_song_by_song_id_name(id, ans[id], './data/')


# 操作步骤：先输入榜单id，再输入A下载当前榜单全部歌曲
if __name__ == "__main__":
    main()
