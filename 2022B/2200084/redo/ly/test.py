import plotly.graph_objects as go

# 定义节点和链接
nodes = {
    "label": ["The Glen Canyon Dam", "California", "The Hoover Dam", "Arizona", "California", "Wyoming", "New Mexico", "Colorado",
              "AZ agriculture", "AZ residential", "CA agriculture", "CA industry", "CA residential", "WY agriculture", "WY industry",
              "NM agriculture", "NM residential", "CO agriculture", "CO residential"]
}

links = {
    "source": [0, 1, 2, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    "target": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    "value": [8, 4, 2, 2, 8, 4, 2, 2, 8, 4, 2, 2, 8, 4, 2, 2, 8, 4, 2]
}

# 创建 Sankey 图
fig = go.Figure(data=[go.Sankey(
    node=nodes,
    link=links
)])

fig.update_layout(title_text="Sankey Diagram", font_size=10)
fig.show()
