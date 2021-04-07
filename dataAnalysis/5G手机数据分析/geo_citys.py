from pyecharts.commons.utils import JsCode
from pyecharts import options as opts
from pyecharts.charts import Geo
from collections import Counter

# 电信5G商用城市名单
Telecom = '北京、天津、上海、重庆、石家庄、保定、太原、晋城、呼和浩特、沈阳、大连、长春、哈尔滨、南京、无锡、苏州、杭州、宁波、温州、嘉兴、合肥、芜湖、福州、厦门、泉州、南昌、鹰潭、济南、青岛、郑州、南阳、武汉、长沙、株洲、广州、深圳、佛山、东莞、南宁、柳州、海口、琼海、成都、贵阳、昆明、西安、兰州、西宁、银川、乌鲁木齐'
# 移动5G商用城市名单
Mobile = '北京、天津、上海、重庆、石家庄、保定、太原、晋城、呼和浩特、沈阳、大连、长春、哈尔滨、南京、无锡、苏州、杭州、宁波、温州、嘉兴、合肥、芜湖、福州、厦门、泉州、南昌、鹰潭、济南、青岛、郑州、南阳、武汉、长沙、株洲、广州、深圳、佛山、东莞、柳州、南宁、海口、琼海、成都、贵阳、昆明、西安、兰州、西宁、银川、乌鲁木齐、'
# 移动5G商用城市名单
Unicom = '北京、上海、广州、深圳、杭州、南京、天津、武汉、济南、郑州、苏州、青岛、重庆、成都、宁波、温州、嘉兴、绍兴、东莞、佛山、中山、珠海、无锡、常州、南通、沈阳、长沙、大连、兰州、福州、石家庄、太原、西宁、西安、厦门、贵阳、保定、呼和浩特、南宁、海口、哈尔滨、南昌、合肥、银川、昆明、长春、泉州、柳州、鹰潭、乌鲁木齐、'

# 处理数据，拼接-分割
mStr = Mobile + Unicom + Telecom
mStr = mStr.split("、")

# 城市计数
citys = []
counts = Counter(mStr)
for i, j in zip(counts, counts.values()):
    citys.append((i, j))
print(citys)
print(len(citys))

# 生成地图
c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", citys, symbol_size=6)
    .set_series_opts(
        # 自定义标签(显示)
        label_opts=opts.LabelOpts(
            formatter=JsCode(
                """
                function(x){
                    console.log(x);
                    if (['福州', '乌鲁木齐', '呼和浩特', '银川', '西宁', '兰州', '成都', '贵阳', '昆明', '南宁', '海口', '长沙', '南昌', '武汉', '合肥', '郑州', '济南', '太原', '石家庄', '天津', '北京', '大连', '沈阳', '长春', '哈尔滨'].indexOf(x.data.name) > -1) {
                        return x.data.name
                    }
                    else {
                        return ''
                    }
                }
                """
            ),
            color='black'
        )
    )
    .set_global_opts(
        # 视觉映射配置，分段型
        visualmap_opts=opts.VisualMapOpts(is_show=True, is_piecewise=True, pieces=[{"value": 1, "color": '#F95DBA', "label": '1个运营商支持', "symbol": 'circle', "symbolSize": 6}, {"value": 2, "color": '#A64DFF', "label": '2个运营商支持', "symbol": 'circle', "symbolSize": 6}, {"value": 3, "color": '#4E70F0', "label": '3个运营商支持', "symbol": 'circle', "symbolSize": 6}], pos_left='22%', pos_bottom='7%'),
        # 图表标题及副标题
        title_opts=opts.TitleOpts(title="目前提供5G商用网络的城市", subtitle='数据来源：电信、移动、联通官方发布', pos_left='center', pos_top='-1%', item_gap=5),
        # 隐藏图例
        legend_opts=opts.LegendOpts(is_show=False),
        # 添加多个文本
        graphic_opts=[
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left='68%', top='52%', z=99),
                children=[
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(left='68%', top='52%', z=100),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text='江浙沪共10\n个城市拥有\n商用5G网络',
                            font='bolder 14px Microsoft YaHei',
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="black"))
                    )
                ],
            ),
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left='68%', top='61%', z=99),
                children=[
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(left='68%', top='61%', z=100),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text='上海 杭州 南京\n苏州 无锡 南通 常州\n宁波 温州 嘉兴 绍兴',
                            font='lighter 12px Microsoft YaHei',
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="black"))
                    )
                ],
            ),
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left='58%', top='84%', z=99),
                children=[
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(left='58%', top='84%', z=100),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text='广东5G商用城市\n最多(6个)',
                            font='bolder 14px Microsoft YaHei',
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="black"))
                    )
                ],
            ),
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left='58%', top='90%', z=99),
                children=[
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(z=100),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text='广州 深圳 佛山 东莞 中山 珠海',
                            font='lighter 12px Microsoft YaHei',
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="black"))
                    )
                ],
            ),
            opts.GraphicGroup(
                graphic_item=opts.GraphicItem(left='23%', top='63%', z=99),
                children=[
                    opts.GraphicText(
                        graphic_item=opts.GraphicItem(z=100),
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            text='西藏是目前唯一没有\n商用网络的省份',
                            font='bolder 14px Microsoft YaHei',
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(fill="black"))
                    )
                ]
            )
        ]
    )
    .render("目前提供5G商用网络的城市.html")
)