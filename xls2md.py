# 将excel文件转换为markdown文件
# 1. 读取excel文件
# 2. 将excel文件转换为markdown文件
# 3. 将markdown文件保存到指定路径

import pandas as pd
import os
from markitdown import MarkItDown

# 读取excel文件
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# 将excel文件转换为markdown文件
def excel_to_markdown(df, file_path):
    df.to_markdown(file_path, index=False)

# 将markdown文件保存到指定路径
def save_markdown(file_path, save_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 使用pandas库进行转换
def convert_with_pandas():
    file_path = 'G3Protocol.xlsx'
    df = read_excel(file_path)
    markdown_file_path = 'data.md'
    excel_to_markdown(df, markdown_file_path)
    save_path = 'data.md'
    save_markdown(markdown_file_path, save_path)

# 使用markitdown库进行转换
def convert_with_markitdown():
    file_path = 'G3Protocol.xlsx'
    md = MarkItDown()
    result = md.convert(file_path)
    with open('data2.md', 'w', encoding='utf-8') as f:
        f.write(result.text_content)

if __name__ == '__main__':
    # convert_with_pandas()
    convert_with_markitdown()


    