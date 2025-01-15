from pyecharts import options as opts
from pyecharts.charts import Sunburst

data = {
    "name": "root",
    "children": [
        {"name": "A", "value": 10},
        {"name": "B", "value": 20},
        {"name": "C", "value": 15},
        {"name": "D", "value": 25},
    ],
}

sunburst = Sunburst()
sunburst.add("", data['children'], radius=[0, "90%"])
sunburst.set_global_opts(title_opts=opts.TitleOpts(title="基本旭日图"))
sunburst.render("basic_sunburst.html")