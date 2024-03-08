import os
import pandas as pd
import numpy as np

file_name = '石药.xlsx'
file_path = os.path.join(os.path.expanduser("~"), 'Desktop', file_name)

# 当查询出来的数据，单条：series格式；多条：dataFrame

# 当只有一个sheet时，只传递文件路径，多个sheet时需要传入sheet_name(序号或名称)，否则查出sheet名称列表
# 二维数据，多行多列
df = pd.read_excel(file_path, sheet_name=1)

print('*' * 40, '读取全表', '*' * 40)
print(df)

print('*' * 40, '读取行索引', '*' * 40)
print('index = ', df.index)

print('*' * 40, '读取列索引', '*' * 40)
print('columns = ', df.columns)

print('*' * 40, '读取一行数据', '*' * 40)
print(df.loc[1])

print('*' * 40, '读取多行数据', '*' * 40)
# 1，2，3行
print(df.loc[1:3])

print('*' * 40, '预处理数据(处理失败，待确认原因)', '*' * 40)
df.loc[:, '严重程度（CTCAE分级）(AETOXGR)'] = df['严重程度（CTCAE分级）(AETOXGR)'].replace('级', '').astype('string')
print(df.dtypes)

# df.loc真是一个功能强大的查询方法
print('*' * 40, '精确查询一行一列的数据', '*' * 40)
print(df.loc[0, 'SubjectName'])

print('*' * 40, '精确查询一行多列列的数据', '*' * 40)
# 行和列都可以传入一个查询列表，同时也可以传入区间:
print(df.loc[0, ['FormOID', 'Study', 'SubjectName']])

# 新增一列（为什么某一列为空，新增的列就全是空数据了？）
df.loc[:, 'new1'] = df['Study'] + df['先天性异常或者出生缺陷(AESCONG)'] + df['其他严重或重要医学事件(AESMIE)']
# 新增一列，apply（传入方法） 或者 assign 或者新增一列，然后赋值


print('*' * 40, '数字列统计结果', '*' * 40)
print(df.describe())
