import pandas as pd

df = pd.read_csv('D:\大作业\dishonest.csv')
df.drop_duplicates(inplace=True)
# print(df.duplicated().sum())      查找数据中是否有重复项
# print(df.info())
df.to_csv('去重后数据.csv',index=False,encoding='utf-8')