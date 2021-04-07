from pyecharts.charts import PictorialBar
from pyecharts import options as opts

# 品牌名称
label = ['华硕', '联想', '摩托罗拉', '魅族', '黑鲨', '努比亚', '中兴', '一加', '小米', 'IQOO', '红米', '三星', 'realme', 'OPPO', '荣耀', 'vivo', '华为']


def pic_bar_microchip(values, label):
    pictorialbar=PictorialBar(init_opts=opts.InitOpts(width='480px', height='700px'))
    pictorialbar.add_xaxis(label)
    pictorialbar.add_yaxis("",
        values[0],
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0,0],
        is_symbol_clip=True,
        symbol='rect',
        color='#F95DBA',
        gap='-100%',
        symbol_margin=10,
        label_opts=opts.LabelOpts(is_show=False)
    )
    pictorialbar.add_yaxis("高通骁龙",
        values[1],
        symbol_size=18,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='#FFCE2B',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.add_yaxis("联发科天玑/MT",
        values[2],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat='20',
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol='rect',
        color='#009688',
        gap='-100%',
        symbol_margin=10
    )
    pictorialbar.add_yaxis("华为麒麟",
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
    pictorialbar.add_yaxis("三星Exynos",
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
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(is_show=True, axistick_opts=opts.AxisTickOpts(is_show=False)),
        legend_opts=opts.LegendOpts(pos_bottom='9%', pos_right='10%', orient='vertical', item_width=18, item_height=18),
        title_opts=opts.TitleOpts(title='各品牌5G手机芯片比较', pos_left='center', pos_top='2%')
    )
    pictorialbar.reversal_axis()
    pictorialbar.render('各品牌5G手机芯片比较.html')


values = [
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [5, 10, 10, 15, 15, 15, 15, 15, 35, 35, 40, 45, 45, 50, 60, 65, 85],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 15, 5, 20, 15, 60, 30, 85],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 45, 25, 60],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 25, 0]
]
pic_bar_microchip(values, label)
