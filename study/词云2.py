# coding=utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文件
f = open("wendang.txt", encoding="utf-8")
text = f.read()

# 生成对象
wc = WordCloud(font_path="C:\\Windows\\Fonts\\STFANGSO.TTF",).generate(text=text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存文件
wc.to_file('wordcloud.png')
