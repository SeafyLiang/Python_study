from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

c = (
    Bar()
        # 添加类目轴文本标签
        .add_xaxis(['中 国\n联 通', '中 国\n电 信', '中 国\n移 动'])
        # 添加数值轴，label显示及偏移，颜色渐变，定义不同类型间距(最新版本pyecharts1.8.1)
        .add_yaxis("4G", [13.29, 14.53, 11.19], itemstyle_opts=JsCode('ItemStyleOpts_4G'),
                   label_opts=opts.LabelOpts(is_show=True, formatter=JsCode('label_4G'), position='insideRight',
                                             color='black', font_weight='bolder', distance=0, font_size=14),
                   category_gap='70%', gap='20%')
        .add_yaxis("5G", [32.57, 32.35, 43.6], itemstyle_opts=JsCode('ItemStyleOpts_5G'),
                   label_opts=opts.LabelOpts(is_show=True, formatter=JsCode('label_5G'), position='insideRight',
                                             color='black', font_weight='bolder', distance=0, font_size=14),
                   category_gap='70%', gap='20%')
        # x/y轴互换位置
        .reversal_axis()
        .set_global_opts(
        # 标题设置
        title_opts=opts.TitleOpts(title='三大运营商的5G/4G速度对比', subtitle='上传网速对比(单位：Mbps)', pos_left='center', pos_top='-1%',
                                  item_gap=3),
        # 隐藏图例
        legend_opts=opts.LegendOpts(is_show=False),
        # x轴属性设置，隐藏刻度线和坐标轴，设置分割线(虚线)
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=True, position='10%'),
                                 position='top',
                                 axistick_opts=opts.AxisTickOpts(is_show=False),
                                 axisline_opts=opts.AxisLineOpts(is_show=False),
                                 splitline_opts=opts.SplitLineOpts(is_show=True,
                                                                   linestyle_opts=opts.LineStyleOpts(width=1,
                                                                                                     opacity=0.5,
                                                                                                     type_='dotted',
                                                                                                     color='grey'))
                                 ),
        # y轴属性设置，隐藏刻度线
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=True, font_size=15, font_weight='normal'),
                                 axistick_opts=opts.AxisTickOpts(is_show=False)),

    )
        # 添加标签函数及颜色函数
        .add_js_funcs(
        """
        const label_4G = function(arg) {
            console.log(arg)
            if (arg.data === 11.19) {
                return '4G▐'
            }
            else {
                return '▐'
            }
        }

        const label_5G = function(arg) {
            //console.log(arg)
            if (arg.data === 43.6) {
                return '5G▐'
            }
            else {
                return '▐'
            }
        }

        const ItemStyleOpts_4G = {'color': function(arg) {
            return new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                {
                    offset: 0.005,
                    color: "black",
                },
                {
                    offset: 0.0058,
                    color: "white",
                },
                {
                    offset: 1,
                    color: '#F7A1AC',
                }
            ])
        }}

        const ItemStyleOpts_5G = {'color': function(arg) {
            return new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                {
                    offset: 0.001,
                    color: "black",
                },
                {
                    offset: 0.003,
                    color: "white",
                },
                {
                    offset: 1,
                    color: '#4E70F0',
                }
            ])
        }}
        """
    )
        .render("三大运营商的速度对比(上传).html")
)
