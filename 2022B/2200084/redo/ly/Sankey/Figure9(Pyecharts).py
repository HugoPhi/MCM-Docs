from pyecharts.charts import Sankey
from pyecharts import options as opts

# 定义节点和链接数据
nodes = [
    {"name": "The Glen Canyon Dam"}, {"name": "The Hoover Dam"},
    {"name": "Arizona"}, {"name": "California"}, {"name": "Wyoming"},
    {"name": "New Mexico"}, {"name": "Colorado"},
    {"name": "AZ_agriculture"}, {"name": "AZ_industry"}, {"name": "AZ_residential"},
    {"name": "CA_agriculture"}, {"name": "CA_industry"}, {"name": "CA_residential"},
    {"name": "WY_agriculture"}, {"name": "WY_industry"}, {"name": "WY_residential"},
    {"name": "NM_agriculture"}, {"name": "NM_industry"}, {"name": "NM_residential"},
    {"name": "CO_agriculture"}, {"name": "CO_industry"}, {"name": "CO_residential"}
]

links = [
    {"source": "The Glen Canyon Dam", "target": "Wyoming", "value": 20},
    {"source": "The Hoover Dam", "target": "Arizona", "value": 8},
    {"source": "The Hoover Dam", "target": "California", "value": 60},
    {"source": "The Hoover Dam", "target": "New Mexico", "value": 5},
    {"source": "The Hoover Dam", "target": "Colorado", "value": 22},
    {"source": "Arizona", "target": "AZ_agriculture", "value": 5},
    {"source": "Arizona", "target": "AZ_industry", "value": 1},
    {"source": "Arizona", "target": "AZ_residential", "value": 2},
    {"source": "California", "target": "CA_agriculture", "value": 45},
    {"source": "California", "target": "CA_industry", "value": 5},
    {"source": "California", "target": "CA_residential", "value": 10},
    {"source": "Wyoming", "target": "WY_agriculture", "value": 18},
    {"source": "Wyoming", "target": "WY_industry", "value": 1},
    {"source": "Wyoming", "target": "WY_residential", "value": 1},
    {"source": "New Mexico", "target": "NM_agriculture", "value": 4},
    {"source": "New Mexico", "target": "NM_industry", "value": 1},
    {"source": "New Mexico", "target": "NM_residential", "value": 1},
    {"source": "Colorado", "target": "CO_agriculture", "value": 18},
    {"source": "Colorado", "target": "CO_industry", "value": 3},
    {"source": "Colorado", "target": "CO_residential", "value": 1}
]

# 创建 Sankey 图
sankey = Sankey(init_opts=opts.InitOpts(width="800px", height="600px"))
sankey.add(
    series_name="Water Distribution",
    nodes=nodes,
    links=links,
    linestyle_opt=opts.LineStyleOpts(opacity=0.2, curve=0.5, color="source"),
    label_opts=opts.LabelOpts(position="right"),
)
sankey.set_global_opts(
    title_opts=opts.TitleOpts(title="Water Distribution Sankey Diagram",pos_top="95%", pos_left="center"),
)

# 渲染图表到本地文件
sankey.render("sankey_water_distribution.html")
