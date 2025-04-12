import pandas as pd
import numpy as np
import os
import re

# 创建输出文件夹
output_dir = './npy_output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 读取原始Excel文件
df = pd.read_excel('./resample.xlsx')

# 遍历每一行
for idx, row in df.iterrows():
    try:
        # 获取字符串并清理格式
        data_str = str(row.iloc[0])
        
        # 使用正则表达式提取所有数字（包括科学计数法）
        numbers = re.findall(r'-?\d+\.?\d*e?[+-]?\d*', data_str)
        
        # 将字符串转换为浮点数
        numbers = [float(x) for x in numbers]
        
        # 确保数据长度正确
        if len(numbers) == 600:  # 200行 × 3列
            # 重塑为200×3的矩阵
            matrix = np.array(numbers).reshape(200, 3)
            
            # 直接保存为.npy格式
            output_file = os.path.join(output_dir, f'resample_{idx+1}.npy')
            np.save(output_file, matrix)
            
            print(f'已成功处理并保存文件: resample_{idx+1}.npy')
        else:
            print(f'第 {idx+1} 行数据长度不正确: {len(numbers)}')
            
    except Exception as e:
        print(f'处理第 {idx+1} 行时出错: {str(e)}')

print('处理完成！')