from pyecharts.charts import PictorialBar
from pyecharts import options as opts

# 品牌名称
label = ['华硕', '联想', '摩托罗拉', '魅族', '黑鲨', '努比亚', '中兴', '一加', '小米', 'IQOO', '红米', '三星', 'realme', 'OPPO', '荣耀', 'vivo', '华为']


def pic_bar_price(values, label):
    """
    5G手机价位比较
    """
    # 初始化，设置图表大小
    pictorialbar = PictorialBar(init_opts=opts.InitOpts(width='480px', height='700px'))
    # x轴标签信息
    pictorialbar.add_xaxis(label)
    # 添加象形图
    pictorialbar.add_yaxis("",
        values[0],
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0,0],
        is_symbol_clip=True,
        symbol='rect',
        color='#FCA46A',
        gap='-100%',
        symbol_margin=10,
        label_opts=opts.LabelOpts(is_show=False)
    )
    pictorialbar.add_yaxis("5000元及以上",
        values[1],
        symbol_size=18,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='#F95DBA',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.add_yaxis("3000-4999元",
        values[2],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='#4E70F0',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.add_yaxis("1000-2999元",
        values[3],
        yaxis_index=0,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='#1720D1',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.add_yaxis("999元及以下",
        values[4],
        yaxis_index=0,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='white',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.set_global_opts(
        # 隐藏x坐标轴
        xaxis_opts=opts.AxisOpts(is_show=False),
        # 显示y坐标轴，隐藏刻度线
        yaxis_opts=opts.AxisOpts(is_show=True, axistick_opts=opts.AxisTickOpts(is_show=False)),
        # 显示图例，设置图例位置
        legend_opts=opts.LegendOpts(pos_bottom='9%', pos_right='10%', orient='vertical', item_width=18, item_height=18),
        # 添加标题，设置标题位置
        title_opts=opts.TitleOpts(title='各品牌5G手机价位比较', pos_left='center', pos_top='2%')
    )
    pictorialbar.reversal_axis()
    pictorialbar.render('各品牌5G手机价位比较.html')


values = [
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [5, 10, 10, 15, 15, 15, 15, 15, 35, 35, 40, 45, 45, 50, 60, 65, 85],
    [0, 10, 5, 15, 15, 15, 15, 10, 25, 35, 40, 10, 45, 40, 60, 50, 55],
    [0, 0, 0, 0, 0, 5, 15, 5, 5, 15, 35, 10, 30, 25, 45, 30, 35],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0]
]
pic_bar_price(values, label)

