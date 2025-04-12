import pandas as pd
import os

def excel_to_csv(excel_path, output_dir=None):
    """
    将Excel文件转换为CSV文件
    :param excel_path: Excel文件路径
    :param output_dir: 输出目录，默认与Excel文件相同
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(excel_path)
        
        # 如果没有指定输出目录，使用Excel文件所在目录
        if output_dir is None:
            output_dir = os.path.dirname(excel_file)
        
        # 构建输出文件路径
        file_name = os.path.splitext(os.path.basename(excel_path))[0]
        csv_path = os.path.join(output_dir, f"{file_name}.csv")
        
        # 将数据框保存为CSV文件
        df.to_csv(csv_path, index=False, encoding='utf-8')
        print(f"转换成功！CSV文件保存在: {csv_path}")
        
    except Exception as e:
        print(f"转换过程中出现错误: {str(e)}")

if __name__ == "__main__":
    # 示例用法
    excel_file = "resample_1.xlsx"
    output_directory = "./"
    
    if output_directory == "":
        output_directory = None
    
    excel_to_csv(excel_file, output_directory)