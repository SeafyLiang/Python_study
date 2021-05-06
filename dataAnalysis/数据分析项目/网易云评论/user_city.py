import pandas as pd
from pyecharts import Map


def city_group(cityCode):
    """
    城市编码
    """
    city_map = {
        '11': '北京',
        '12': '天津',
        '31': '上海',
        '50': '重庆',
        '5e': '重庆',
        '81': '香港',
        '82': '澳门',
        '13': '河北',
        '14': '山西',
        '15': '内蒙古',
        '21': '辽宁',
        '22': '吉林',
        '23': '黑龙江',
        '32': '江苏',
        '33': '浙江',
        '34': '安徽',
        '35': '福建',
        '36': '江西',
        '37': '山东',
        '41': '河南',
        '42': '湖北',
        '43': '湖南',
        '44': '广东',
        '45': '广西',
        '46': '海南',
        '51': '四川',
        '52': '贵州',
        '53': '云南',
        '54': '西藏',
        '61': '陕西',
        '62': '甘肃',
        '63': '青海',
        '64': '宁夏',
        '65': '新疆',
        '71': '台湾',
        '10': '其他',
    }
    cityCode = str(cityCode)
    return city_map[cityCode[:2]]


# 读取数据
# df = pd.read_csv('comment_before.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
df = pd.read_csv('comment_after.csv', header=None, names=['name', 'userid', 'age', 'gender', 'city', 'text', 'comment', 'commentid', 'praise', 'date'], encoding='utf-8-sig')
# 根据评论ID去重
df = df.drop_duplicates('commentid')
# 进行省份匹配
df['location'] = df['city'].apply(city_group)

# 分组汇总
loc_message = df.groupby(['location'])
loc_com = loc_message['location'].agg(['count'])
loc_com.reset_index(inplace=True)

# 绘制地图
value = [i for i in loc_com['count']]
attr = [i for i in loc_com['location']]
# map = Map("歌曲发布后评论用户的地区分布图", title_pos='center', title_top=0)
# map.add("", attr, value, maptype="china", is_visualmap=True, visual_text_color="#000", is_map_symbol_show=False, visual_range=[0, 600])
# map.render('歌曲发布后评论用户的地区分布图.html')
map = Map("歌曲被爆抄袭后评论用户的地区分布图", title_pos='center', title_top=0)
map.add("", attr, value, maptype="china", is_visualmap=True, visual_text_color="#000", is_map_symbol_show=False, visual_range=[0, 600])
map.render('歌曲被爆抄袭后评论用户的地区分布图.html')

