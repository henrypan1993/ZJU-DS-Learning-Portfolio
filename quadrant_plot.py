import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import random
import pandas as pd
import os
import math
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


# 常量配置
@dataclass
class PlotConfig:
    """图表配置类"""
    FIGURE_SIZE: Tuple[float, float] = (15, 12)
    POINT_SIZE: int = 120
    POINT_ALPHA: float = 0.6
    POINT_LINEWIDTH: int = 2
    FONT_SIZE: int = 9
    LINE_ALPHA: float = 0.3
    LINE_WIDTH: float = 1.0
    GRID_ALPHA: float = 0.2
    DPI: int = 300
    
    # 颜色配置
    COLORS = {
        'Q1': '#FF6B6B',  # 右上象限 - 红色
        'Q2': '#4ECDC4',  # 左上象限 - 青色
        'Q3': '#45B7D1',  # 左下象限 - 蓝色
        'Q4': '#96CEB4'   # 右下象限 - 绿色
    }
    
    # 标签配置
    LABEL_OFFSET: float = 0.1
    MAX_RADIUS_RATIO: float = 0.15
    RADIUS_GROWTH: float = 0.2
    ROTATION_ANGLE: float = np.pi/3.5

def cartesian_to_polar(x: float, y: float) -> Tuple[float, float]:
    """将笛卡尔坐标转换为极坐标"""
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, theta

def polar_to_cartesian(r: float, theta: float) -> Tuple[float, float]:
    """将极坐标转换为笛卡尔坐标"""
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def calculate_axis_range(data: Dict[str, List[float]], padding: float = 0.5) -> Tuple[float, float, float, float]:
    """计算坐标轴范围"""
    x_min = min(data['使用频率']) - padding
    x_max = max(data['使用频率']) + padding
    y_min = min(data['酒店相关度']) - padding
    y_max = max(data['酒店相关度']) + padding
    
    # 确保范围至少为4个单位
    x_range = max(4, x_max - x_min)
    y_range = max(4, y_max - y_min)
    
    return x_min, x_max, y_min, y_max

def calculate_label_position(x: float, y: float, x_median: float, y_median: float, 
                           overlap_count: int, overlap_index: int, config: PlotConfig) -> Tuple[float, float, str, str]:
    """
    计算标签位置和对齐方式
    Args:
        x, y: 点的坐标
        x_median, y_median: 中位数
        overlap_count: 重叠点的总数
        overlap_index: 当前点在重叠组中的索引
        config: 配置对象
    Returns:
        offset_x, offset_y, ha, va: 偏移量和对齐方式
    """
    # 根据象限调整标签位置
    if x > x_median:
        ha = 'left'
        offset_x = config.LABEL_OFFSET
    else:
        ha = 'right'
        offset_x = -config.LABEL_OFFSET
    
    if y > y_median:
        va = 'bottom'
        offset_y = config.LABEL_OFFSET
    else:
        va = 'top'
        offset_y = -config.LABEL_OFFSET
    
    # 如果有重叠，使用极坐标系统调整位置
    if overlap_count > 0:
        r, theta = cartesian_to_polar(offset_x, offset_y)
        # 根据重叠次数增加半径
        r *= (1 + overlap_count * config.RADIUS_GROWTH)
        # 根据重叠索引添加固定角度
        theta += overlap_index * config.ROTATION_ANGLE
        offset_x, offset_y = polar_to_cartesian(r, theta)
    
    return offset_x, offset_y, ha, va

def read_data_from_excel(file_path: str) -> Optional[Dict[str, List]]:
    """
    从Excel文件中读取数据
    Args:
        file_path: Excel文件路径
    Returns:
        dict: 包含简短标题、使用频率和酒店相关度的字典
    """
    try:
        df = pd.read_excel(file_path, sheet_name="数据处理")
        data = {
            '简短标题': df['简短标题'].tolist(),
            '使用频率': df['使用频率'].tolist(),
            '酒店相关度': df['酒店相关度'].tolist()
        }
        return data
    except Exception as e:
        print(f"读取数据时出错: {str(e)}")
        return None

def create_quadrant_plot(data: Dict[str, List], config: PlotConfig = PlotConfig()) -> None:
    """
    创建四象限图
    Args:
        data: 包含简短标题、使用频率和酒店相关度的字典
        config: 图表配置对象
    """
    # 计算中位数
    x_median = np.median(data['使用频率'])
    y_median = np.median(data['酒店相关度'])

    # 创建图形
    plt.figure(figsize=config.FIGURE_SIZE)

    # 计算坐标轴范围
    x_min, x_max, y_min, y_max = calculate_axis_range(data)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    # 根据象限设置不同的颜色
    colors = []
    for x, y in zip(data['使用频率'], data['酒店相关度']):
        if x > x_median and y > y_median:
            colors.append(config.COLORS['Q1'])
        elif x <= x_median and y > y_median:
            colors.append(config.COLORS['Q2'])
        elif x <= x_median and y <= y_median:
            colors.append(config.COLORS['Q3'])
        else:
            colors.append(config.COLORS['Q4'])

    # 绘制散点图
    plt.scatter(data['使用频率'], data['酒店相关度'], 
                c=colors, s=config.POINT_SIZE, alpha=config.POINT_ALPHA,
                edgecolor='white', linewidth=config.POINT_LINEWIDTH)

    # 使用numpy数组优化重叠检查
    points = np.column_stack((data['使用频率'], data['酒店相关度']))
    overlap_matrix = np.zeros((len(points), len(points)), dtype=bool)
    
    # 向量化计算重叠矩阵
    for i in range(len(points)):
        overlap_matrix[i] = (np.abs(points[:, 1] - points[i, 1]) < 0.2) & \
                          (np.abs(points[:, 0] - points[i, 0]) < 0.2)
    
    # 添加标签
    for i, (txt, x, y) in enumerate(zip(data['简短标题'], data['使用频率'], data['酒店相关度'])):
        # 计算当前点与之前点的重叠情况
        overlap_count = np.sum(overlap_matrix[i, :i])
        overlap_index = np.sum(overlap_matrix[i, :i+1]) - 1  # 当前点在重叠组中的索引
        
        # 计算标签位置
        offset_x, offset_y, ha, va = calculate_label_position(x, y, x_median, y_median, 
                                                            overlap_count, overlap_index, config)
        
        # 计算标签位置（使用数据坐标）
        label_x = x + offset_x
        label_y = y + offset_y
        
        # 确保标签在图表范围内
        label_x = max(x_min, min(x_max, label_x))
        label_y = max(y_min, min(y_max, label_y))
        
        # 添加标签
        plt.annotate(txt, 
                    xy=(x, y),
                    xytext=(label_x, label_y),
                    textcoords='data',
                    ha=ha,
                    va=va,
                    fontsize=config.FONT_SIZE,
                    color=colors[i],
                    arrowprops=dict(arrowstyle='-',
                                  color=colors[i],
                                  alpha=config.LINE_ALPHA,
                                  linewidth=config.LINE_WIDTH))

    # 绘制象限线
    plt.axvline(x=x_median, color='gray', linestyle='--', alpha=config.GRID_ALPHA, linewidth=config.LINE_WIDTH)
    plt.axhline(y=y_median, color='gray', linestyle='--', alpha=config.GRID_ALPHA, linewidth=config.LINE_WIDTH)

    # 设置标题和轴标签
    plt.title('功能四象限分析图', fontsize=16, pad=20)
    plt.xlabel('使用频率', fontsize=12)
    plt.ylabel('酒店相关度', fontsize=12)

    # 添加网格
    plt.grid(True, linestyle='--', alpha=config.GRID_ALPHA)

    # 调整布局
    plt.tight_layout()

    # 保存图片
    plt.savefig('quadrant_plot.png', dpi=config.DPI, bbox_inches='tight')
    plt.close()

    # 打印调试信息
    print(f"总共获取到{len(data['简短标题'])}个数据")
    print("所有点的坐标：")
    for txt, x, y in zip(data['简短标题'], data['使用频率'], data['酒店相关度']):
        print(f"{txt}: ({x}, {y})")

def main():
    # 设置中文字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    
    file_path = r"C:\Users\panhe\Desktop\AI应用方向校对_20250328.xlsx"
    if not os.path.exists(file_path):
        print("文件不存在")
        return
    
    print("文件存在，开始读取数据...")
    data = read_data_from_excel(file_path)
    if data is None:
        print("数据读取失败，程序退出！")
        return
    
    create_quadrant_plot(data)
    print("四象限图已生成，保存为 quadrant_plot.png")

if __name__ == "__main__":
    main() 