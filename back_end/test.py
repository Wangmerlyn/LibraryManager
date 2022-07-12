# -*- coding:utf-8 -*-
"""
作者：陈景行
日期：2022年07月04日
主题：
"""
import pandas as pd

data = pd.read_csv('books.csv', encoding='utf-8', error_bad_lines=False)
with open('test.txt', 'a+', encoding='utf-8') as f:    # 现在jupyter新建一个txt空文档
    for line in data.values:
        f.write((str(line[4])+','+str(line[1])+','+str(line[2])+','+str(line[11])+','+str(line[10])+'\n'))
        #展示五列 ，如果不能用str，可以先cast as varchar(20)