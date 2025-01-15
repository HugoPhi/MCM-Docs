from pyecharts import options as opts
from pyecharts.charts import Sunburst

# 数据
data = [
    {
        "name": "Arizona",
        "value": 11.96,
        "children": [
            {"name": "Agriculture", "value": 9.24},
            {"name": "Industry", "value": 0.28},
            {"name": "Residential", "value": 2.45},
        ],
    },
    {
        "name": "California",
        "value": 50.0,
        "children": [
            {"name": "Agriculture", "value": 39.8},
            {"name": "Industry", "value": 6.2},
            {"name": "Residential", "value": 4.0},
        ],
    },
    {
        "name": "Colorado",
        "value": 16.0,
        "children": [
            {"name": "Agriculture", "value": 14.37},
            {"name": "Industry", "value": 1.0},
            {"name": "Residential", "value": 0.62},
        ],
    },
    {
        "name": "New Mexico",
        "value": 14.0,
        "children": [
            {"name": "Agriculture", "value": 13.47},
            {"name": "Industry", "value": 0.35},
            {"name": "Residential", "value": 0.18},
        ],
    },
    {
        "name": "Wyoming",
        "value": 8.0,
        "children": [
            {"name": "Agriculture", "value": 7.51},
            {"name": "Industry", "value": 0.12},
            {"name": "Residential", "value": 0.37},
        ],
    },
]

# 创建旭日图
sunburst = Sunburst()
sunburst.add(
    "",
    data,
    radius=[0, "60%"],  # 调整图表大小
    center=["50%", "50%"],  # 调整图表位置
    levels=[
        {},
        {},
        {
            "label": {
                "formatter": "{b}: {c}%",
                "position": "outside",

            },
            "labelLine": opts.PieLabelLineOpts(  # 启用标签引导线
                length=40,  # 线的长度
            )
        }
    ]
)
sunburst.set_global_opts(
    title_opts=opts.TitleOpts(
        title="Water Usage by Sector in Different States",
        pos_left="center",  # 标题位置水平居中
        pos_top="5%",  # 标题位置距离顶部5%
    )
)
# 渲染图表
sunburst.render("water_usage_sunburst.html")