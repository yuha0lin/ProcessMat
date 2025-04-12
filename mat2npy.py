import scipy.io
import numpy as np
import os
import re

# 基础输出目录
base_output_dir = './npy_one_step'
if not os.path.exists(base_output_dir):
    os.makedirs(base_output_dir)

# 获取所有.mat文件
mat_dir = './cluster_results'
mat_files = [f for f in os.listdir(mat_dir) if f.endswith('.mat')]

# 处理每个.mat文件
for mat_file in mat_files:
    # 创建对应的输出子文件夹
    mat_name = os.path.splitext(mat_file)[0]  # 获取不带扩展名的文件名
    output_dir = os.path.join(base_output_dir, mat_name)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 读取.mat文件
    mat_path = os.path.join(mat_dir, mat_file)
    mat_data = scipy.io.loadmat(mat_path)
    
    # 移除系统变量
    data_dict = {k: v for k, v in mat_data.items() if not k.startswith('__')}
    
    # 显示变量信息
    print(f"\n处理文件: {mat_file}")
    print("包含的变量：")
    for key, value in data_dict.items():
        print(f"变量名: {key}, 形状: {value.shape}, 类型: {value.dtype}")
    
    # 处理每个变量中的数据
    for key, value in data_dict.items():
        try:
            data = value.flatten()
            matrices = []
            
            for item in data:
                str_data = str(item)
                numbers = re.findall(r'-?\d+\.?\d*e?[+-]?\d*', str_data)
                numbers = [float(x) for x in numbers]
                
                if len(numbers) == 600:
                    matrix = np.array(numbers).reshape(200, 3)
                    matrices.append(matrix)
            
            # 保存到对应的子文件夹中
            for i, matrix in enumerate(matrices):
                output_file = os.path.join(output_dir, f'{key}_{i+1}.npy')
                np.save(output_file, matrix)
                print(f'已保存: {output_file}')
                
        except Exception as e:
            print(f'处理变量 {key} 时出错: {str(e)}')

print('\n所有文件处理完成！')