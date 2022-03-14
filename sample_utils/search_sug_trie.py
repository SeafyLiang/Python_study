#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   search_sug_trie.py
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2022/3/14 18:42   SeafyLiang   1.0        基于前缀树匹配的搜索提示
"""

# 导入包
from pytrie import StringTrie
import pypinyin
import pandas as pd
import time


# 文本转拼音
def pinyin(text):
    """
    :param text: 文本
    :return: 文本转拼音
    """
    gap = ' '
    piny = gap.join(pypinyin.lazy_pinyin(text))
    return piny


# 获取拼音的每个首字母
def get_every_word_first(text):
    """
    :param text:文本
    :return: 返回拼音首字母
    """
    return ''.join([i[0] for i in pinyin(text).split(' ')])


# 获取拼音的第一个首字母
def get_all_pinying(text):
    """
        :param text: 文本
        :return: 文本转拼音
        """
    gap = ''
    piny = gap.join(pypinyin.lazy_pinyin(text))

    return piny


# 自定义字典树类
class Suggester(object):
    def __init__(self):
        self.trie = None
        self.trie = StringTrie()

    def update_trie(self, word_list):
        for word in word_list:
            word = word.lower()
            # 拼音提取
            word_pinyin1 = get_every_word_first(word)
            word_pinyin2 = get_all_pinying(word)

            # 拼音建立字典树
            self.trie[word] = word
            self.trie[word_pinyin1] = word_pinyin1
            self.trie[word_pinyin2] = word_pinyin2

    def search_prefix(self, prefix):
        return self.trie.values(prefix=prefix)


# 构建字典树
def build_all_trie(wordlist):
    """
    :param wordlist: 关键词列表
    :return: 字典树和映射数据集
    """
    sug = Suggester()
    sug.update_trie(wordlist)
    data = pd.DataFrame({"word": wordlist})
    data['pinyin1'] = data['word'].apply(lambda x: get_every_word_first(x))
    data['pinyin2'] = data['word'].apply(lambda x: get_all_pinying(x))

    return sug, data


# 判断字符串只包含中文
def check_contain_chinese(check_str):
    flag = True
    for ch in check_str:
        if u'\u4e00' >= ch or ch >= u'\u9fff':
            flag = False
    return flag


# 关键词搜索提示查询
def get_tips_word(sug, data, s):
    """
    :param sug: 字典树
    :param data: 中文和英文映射数据集
    :param s: 搜索词
    :return: 返回搜索提示词
    """
    try:
        if len(s) > 0:
            # 判断输入是否只包含中文，若只中文，按中文查
            if check_contain_chinese(s) is True:
                # 输出结果
                kk = sug.search_prefix(s)
                result3 = data[data['word'].isin(kk)]
                result6 = list(set(result3['word']))
                return result6

            # 若不是只包含中文，转换为英文去查询
            else:
                s1 = get_all_pinying(s)
                kk = sug.search_prefix(s1)
                result1 = data[data['pinyin1'].isin(kk)]
                result2 = data[data['pinyin2'].isin(kk)]
                result3 = data[data['word'].isin(kk)]
                result4 = result1.append(result2, ignore_index=True)
                result5 = result3.append(result4, ignore_index=True)
                # 输出结果
                result6 = list(set(result5['word']))
                return result6
        else:
            return

    except Exception as e:
        print("{0}".format(str(e)))


if __name__ == '__main__':
    wordlist = ['意味深长', '意想不到', '意气用事', '意气风发', '意兴阑珊', '意气高昂', '意气相投', '巴黎恋人', '巴黎圣母院', '巴黎宝贝']

    # 构造字典树
    sug, data = build_all_trie(wordlist)
    time1 = time.time()

    # 搜索词
    s = 'b'

    result = get_tips_word(sug, data, s)
    print(result)

    time2 = time.time()
    print('总共耗时：' + str(time2 - time1) + 's')
