import matplotlib.font_manager as fm

# 获取所有可用的字体
fonts = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# 打印字体列表
for font in fonts:
    print(fm.FontProperties(fname=font).get_name())
