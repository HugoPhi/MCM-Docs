import plotly.graph_objects as go

# 数据
ids = [
    'Arizona', 'California', 'Colorado', 'New Mexico', 'Wyoming',
    'Agriculture - Arizona', 'Industry - Arizona', 'Residential - Arizona',
    'Agriculture - California', 'Industry - California', 'Residential - California',
    'Agriculture - Colorado', 'Industry - Colorado', 'Residential - Colorado',
    'Agriculture - New Mexico', 'Industry - New Mexico', 'Residential - New Mexico',
    'Agriculture - Wyoming', 'Industry - Wyoming', 'Residential - Wyoming'
]
labels = [
    'Arizona', 'California', 'Colorado', 'New Mexico', 'Wyoming',
    'Agriculture', 'Industry', 'Residential',
    'Agriculture', 'Industry', 'Residential',
    'Agriculture', 'Industry', 'Residential',
    'Agriculture', 'Industry', 'Residential',
    'Agriculture', 'Industry', 'Residential',
]
parents = [
    '', '', '', '', '',
    'Arizona', 'Arizona', 'Arizona',
    'California', 'California', 'California',
    'Colorado', 'Colorado', 'Colorado',
    'New Mexico', 'New Mexico', 'New Mexico',
    'Wyoming', 'Wyoming', 'Wyoming'
]
values = [
    (77.0 + 2.3 + 20.4) * 0.12, (79.6 + 12.4 + 8.0) * 0.5, (89.8 + 6.3 + 3.9) * 0.16, (96.2 + 2.5 + 1.3) * 0.14, (93.9 + 1.5 + 4.6) * 0.08,
    77.0 * 0.12, 2.3 * 0.12, 20.4 * 0.12,
    79.6 * 0.5, 12.4 * 0.5, 8.0 * 0.5,
    89.8 * 0.16, 6.3 * 0.16, 3.9 * 0.16,
    96.2 * 0.14, 2.5 * 0.14, 1.3 * 0.14,
    93.9 * 0.08, 1.5 * 0.08, 4.6 * 0.08
]

# 计算百分比值
total_value = sum(values[:5])  # 只取根节点总和
percentages = [f"{(v / total_value * 100):.2f}%" for v in values]

# 颜色
colors = [
    '#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0',
    '#ff9999', '#ff6666', '#ff3333',
    '#66b3ff', '#3399ff', '#0073e6',
    '#99ff99', '#66ff66', '#33cc33',
    '#ffcc99', '#ffb366', '#ff9933',
    '#c2c2f0', '#b3b3ff', '#9999ff'
]

# 创建图表
fig = go.Figure(go.Sunburst(
    ids=ids,
    labels=labels,
    parents=parents,
    values=values,
    marker=dict(colors=colors),
    branchvalues='total',
    texttemplate="%{label}<br>%{customdata}",  # 自定义标签显示格式
    customdata=percentages  # 添加百分比数据

))

# 自定义图表布局
fig.update_layout(
    title_text='Water Usage by Sector in Different States',
    title_x=0.5,
    title_y=0.99,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=40, l=0, r=0, b=0),

)



fig.show()