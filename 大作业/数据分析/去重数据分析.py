import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
import seaborn as sns
import jieba
import re
import collections
from pyecharts.charts import WordCloud

# 地区柱形图
df = pd.read_csv('去重后数据.csv')
count_province = df['area'].value_counts()
matplotlib.rcParams['font.family'] = 'SimHei'
matplotlib.rcParams['font.size'] = 10

sns.barplot(x=count_province.values,y=count_province.index)
plt.show()

# 判处内容词云
# 为了不影响原数据，所以拷贝一份
data = df.copy()
# 去除空格
A = data['content'].str.strip()
data['content'] = A

# 拼接所有岗位类别为数据科学的岗位描述
string_data = ''
for i in data['content']:
    string_data += str(i)

# 2.文本预处理，去除各种标点符号，不然统计词频时会统计进去
# 定义正则表达式匹配模式，其中的|代表或
pattern = re.compile(u'\t|\n| |；|\.|。|：|：\.|-|:|\d|;|、|，|\)|\(|\?|"')
# 将符合模式的字符去除，re.sub代表替换，把符合pattern的替换为空
string_data = re.sub(pattern, '', string_data)

# 3.文本分词
seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词

# 4.运用过滤词表优化掉常用词，比如“的”这些词，不然统计词频时会统计进去
object_list = []

# 读取过滤词表
with open('remove_words.txt', 'w+', encoding="utf-8") as fp:
    remove_words = fp.read().split()

# 循环读出每个分词
for word in seg_list_exact:
    #看每个分词是否在常用词表中或结果是否为空或\xa0不间断空白符，如果不是再追加
    if word not in remove_words and word != ' ' and word != '\xa0':
        object_list.append(word)  # 分词追加到列表

# 5.进行词频统计，使用pyecharts生成词云
# 词频统计
word_counts = collections.Counter(object_list)  # 对分词做词频统计
word_counts_top = word_counts.most_common(100)  # 获取前100最高频的词

# 绘图
# https://gallery.pyecharts.org/#/WordCloud/wordcloud_custom_mask_image
c = (
    WordCloud()
    .add("", word_counts_top)   #根据词频最高的词
    .render("wordcloud.html")   #生成页面
)

# 查询失信名单中个人和企业的个数
df['len_str'] = df['name'].map(lambda x: len(str(x)))
company = 0
person = 0
for i in df['len_str']:
    if i>3:
        company+=1
    if i<=3:
        person+=1
print('失信名单中公司个数有',company,'个')
print('失信名单中个人个数有',person,'个')