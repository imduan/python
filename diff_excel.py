import pandas as pd
import numpy as np

def compare_excel_files(file1, file2, index_cols):
    # 读取 Excel 文件
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)

    # 按照索引列-检查行重复
    duplicate_rows1 = df1[df1.duplicated(subset=index_cols)]
    duplicate_rows2 = df2[df2.duplicated(subset=index_cols)]
    
    if not duplicate_rows1.empty:
        print(f"文件1,按照索引列 {index_cols},重复行: {len(duplicate_rows1)}")
        return
    if not duplicate_rows2.empty:
        print(f"文件2,按照索引列 {index_cols},重复行: {len(duplicate_rows2)}")
        return
        
    # 设置指定列作为索引
    df1 = df1.set_index(index_cols)
    df2 = df2.set_index(index_cols)

    # 检查列名是否一致
    if df1.columns.tolist() != df2.columns.tolist():
        print("两个文件的列名不同，无法准确比较。")
        return

    print("----开始比较两个文件的差集----")
    # 检查索引是否一致
    #if not df1.index.equals(df2.index):
    #    print("两个文件指定索引列的值不同。")
    #    return
    if not df1.index.equals(df2.index):
        # 将索引转换为集合
        set_index_df1 = set(df1.index)
        set_index_df2 = set(df2.index)
        missing_index_df1 = set_index_df2 - set_index_df1
        missing_index_df2 = set_index_df1 - set_index_df2
        if missing_index_df1:
            print(f"文件1 中缺少索引: {missing_index_df1}")
        if missing_index_df2:
            print(f"文件2 中缺少索引: {missing_index_df2}")

    print("----开始比较两个文件的重叠索引的差异----")
    # 找出两个 DataFrame 中共同的索引
    common_index = df1.index.intersection(df2.index)

    # 筛选出具有共同索引的行
    df1_common = df1.loc[common_index]
    df2_common = df2.loc[common_index]

    placeholder = 'nan_placeholder'
    df1_common = df1_common.fillna(placeholder)
    df2_common = df2_common.fillna(placeholder)

    diff = df1_common != df2_common
    diff_indices = diff[diff].stack().index.tolist()

    if diff_indices:
        print(f"发现差异：{len(diff_indices)}")
        for index in diff_indices:
            multi_index = index[:-1]  # 提取多级索引部分
            col = index[-1]  # 提取列名
            print(f"差异 {index} file1:{df1.loc[index]},file2:{df2.loc[index]}")
    else:
        print("两个文件除索引不同的行外，剩余部分没有差异。")

# 示例调用
file1 = 'file1.xlsx'
file2 = 'file2.xlsx'
# 可以指定多列作为索引，这里以两列为例
index_columns = ['业务单据']
compare_excel_files(file1, file2, index_columns)
