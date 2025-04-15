import os
from docx import Document
from docx.shared import Mm
from typing import List, Tuple
import re
import argparse
import sys

def is_word_document(filename: str) -> bool:
    """
    检查文件是否为Word文档
    
    Args:
        filename: 文件名
        
    Returns:
        如果是Word文档返回True，否则返回False
    """
    file_ext = os.path.splitext(filename)[1].lower()
    return file_ext in ['.docx', '.doc']

def collect_documents_by_number(folder_path: str) -> List[str]:
    """
    遍历文件夹收集所有Word文档文件，并按文件名开头的数字序号排序
    
    Args:
        folder_path: 要遍历的文件夹路径
        
    Returns:
        按序号排序的文件路径列表
    """
    # 确保文件夹路径存在
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"文件夹路径不存在: {folder_path}")
    
    # 存储文件信息的列表
    files = []
    
    # 遍历文件夹
    for root, dirs, filenames in os.walk(folder_path):
        for filename in filenames:
            # 只处理Word文档
            if is_word_document(filename):
                file_path = os.path.join(root, filename)
                # 提取文件名开头的数字
                match = re.match(r'^(\d+)', filename)
                if match:
                    number = int(match.group(1))
                    files.append((number, file_path))
    
    # 按数字序号排序
    files.sort(key=lambda x: x[0])
    
    # 只返回文件路径列表
    return [file_path for _, file_path in files]

def merge_documents(input_files: List[str], output_file: str, add_page_breaks: bool = False):
    """
    合并多个Word文档到一个文件
    
    Args:
        input_files: 要合并的Word文档路径列表
        output_file: 输出的合并文档路径
        add_page_breaks: 是否在每个文档之间添加分页符
    """
    # 创建新的Word文档
    word_doc = Document()
    
    # 设置页面大小（宽182mm，长257mm）
    section = word_doc.sections[0]
    section.page_height = Mm(257)
    section.page_width = Mm(182)
    
    # 处理每个输入文件
    for i, file_path in enumerate(input_files):
        try:
            # 添加分页符（除了第一个文档）
            if add_page_breaks and i > 0:
                word_doc.add_page_break()
                
            # 直接复制Word文档内容
            doc = Document(file_path)
            
            # 复制内容
            for element in doc.element.body:
                # 跳过批注
                if element.tag.endswith('commentRangeStart') or \
                   element.tag.endswith('commentRangeEnd') or \
                   element.tag.endswith('commentReference'):
                    continue
                word_doc.element.body.append(element)
        except Exception as e:
            print(f"处理文件 '{file_path}' 时出错: {str(e)}")
            # 继续处理其他文件
    
    # 保存合并后的文档
    try:
        word_doc.save(output_file)
    except Exception as e:
        raise IOError(f"保存合并文档时出错: {str(e)}")

def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='合并多个Word文档到一个文件')
    parser.add_argument('-i', '--input', required=True, help='输入文件夹路径')
    parser.add_argument('-o', '--output', default='merged_document.docx', help='输出文件路径')
    parser.add_argument('-p', '--page-breaks', action='store_true', help='在文档之间添加分页符')
    return parser.parse_args()

def main():
    # 解析命令行参数
    try:
        args = parse_arguments()
        folder_path = args.input
        output_file = args.output
        add_page_breaks = args.page_breaks
    except Exception as e:
        print(f"参数解析错误: {str(e)}")
        return 1
    
    try:
        # 收集所有文档并按序号排序
        sorted_files = collect_documents_by_number(folder_path)
        
        if not sorted_files:
            print("未找到任何Word文档文件！")
            return 1
            
        # 打印找到的文件
        print("\n找到的文件:")
        for i, file_path in enumerate(sorted_files):
            print(f"{i+1}. {os.path.basename(file_path)}")
        
        # 合并所有文件
        merge_documents(sorted_files, output_file, add_page_breaks)
        print(f"\n文档已成功合并到: {output_file}")
        return 0
        
    except FileNotFoundError as e:
        print(f"错误: {str(e)}")
        return 1
    except IOError as e:
        print(f"输入/输出错误: {str(e)}")
        return 1
    except Exception as e:
        print(f"发生未知错误: {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(main()) 