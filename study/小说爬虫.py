import requests
from lxml import etree

# 章节菜单网址
url = "https://www.qqxs.cc/xs/116/116087/"
response = requests.get(url).content.decode("gbk", "ignore")

# 获取页面的HTML数据
dom = etree.HTML(response)
html = dom.xpath("//div/dl/dd/a")

for x in html:
    # 创建一个新字典
    dic = {}
    # 获取小说页面网址
    dic["name"] = x.xpath("./text()")[0]
    # 提取章节名
    dic["url"] = url + x.xpath("./@href")[0]
    # print(dic)
    # 对章节网址进行请求
    response = requests.get(dic["url"]).content.decode("gbk", "ignore")
    # print(response)

    # 提取页面中的HTML数据
    doc = etree.HTML(response)
    # 提取小说文字数据
    HTML = doc.xpath('//div[@class="zhangjieTXT"]/text()')

    # 遍历小说数据
    for v in HTML:
        # 头尾去空格
        novel = v.strip()
        # 打开“小说”文件夹，将小说的章节名作为保存的文件名，以“a”追加的方式，编码成“utf-8”
        f = open("小说/" + dic['name'] + ".txt", "a", encoding="utf-8")
        # 写入小说数据，\n是换行符
        f.write(novel + "\n")
        # 关闭读写文件
        f.close()
