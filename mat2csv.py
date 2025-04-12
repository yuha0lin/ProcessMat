import scipy.io
import pandas as pd

# 读取.mat文件
mat_data = scipy.io.loadmat('resample.mat')

# 移除系统变量（以'__'开头的变量）
data_dict = {k: v for k, v in mat_data.items() if not k.startswith('__')}

# 显示.mat文件中的变量信息
print("文件中包含的变量：")
for key, value in data_dict.items():
    print(f"变量名: {key}, 形状: {value.shape}, 类型: {value.dtype}")

# 将数据转换为DataFrame
df = pd.DataFrame()
for key, value in data_dict.items():
    if value.shape[1] == 1:  # 如果是列向量
        df[key] = value.flatten()
    else:  # 如果是矩阵，为每一列创建单独的列
        for i in range(value.shape[1]):
            df[f'{key}_{i+1}'] = value[:, i]

# 保存为CSV文件
df.to_csv('resample.csv', index=False)
print('转换完成！数据已保存到 resample.csv')