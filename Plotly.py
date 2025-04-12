import plotly.graph_objects as go
import numpy as np
import os

# 创建一个空的Figure对象
fig = go.Figure()

# 定义颜色映射（除了noise使用红色外，其他使用不同颜色）
colors = ['blue', 'green', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'brown']

# 读取npy_one_step文件夹中的所有子文件夹
npy_dir = './npy_one_step'
for cluster_folder in sorted(os.listdir(npy_dir)):
    cluster_path = os.path.join(npy_dir, cluster_folder)
    
    if os.path.isdir(cluster_path):
        # 确定颜色
        if cluster_folder == 'cluster_noise':
            color = 'red'
        else:
            # 从cluster_文件夹名称中提取数字
            try:
                cluster_num = int(cluster_folder.split('_')[1]) - 1
                color = colors[cluster_num % len(colors)]  # 循环使用颜色列表
            except:
                continue
        
        # 处理该文件夹中的所有npy文件
        for file in os.listdir(cluster_path):
            if file.endswith('.npy'):
                # 读取轨迹数据
                points = np.load(os.path.join(cluster_path, file))
                x, y, z = points[:,0], points[:,1], points[:,2]
                
                # 添加轨迹到图中
                fig.add_trace(go.Scatter3d(
                    x=x, y=y, z=z,
                    mode='lines',
                    line=dict(color=color, width=1),
                    name=f'{cluster_folder}_{file}',  # 使用文件夹名和文件名作为图例
                    showlegend=False  # 隐藏该轨迹的图例
                ))

# 优化布局
fig.update_layout(
    scene=dict(
        # aspectmode='data',  # 保持实际比例
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        bgcolor='rgba(0,0,0,0)'  # 设置3D场景为透明背景
    ),
    paper_bgcolor='rgba(0,0,0,0)',  # 设置整个画布为透明背景
    showlegend=False
)

# 显示图形
fig.show()
fig_json = fig.to_json()
with open("d:/college/wxh/Core/plotly_data.json", "w") as f:
    f.write(fig_json)