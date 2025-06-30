"""
目录内容查询工具
根据指定的系统完整目录，列出目录下所有的子目录名称和文件名的完整系统路径
"""

import os
import logging
from typing import Dict, List, Any
from typing_extensions import Annotated

logger = logging.getLogger(__name__)


def list_directory_contents(
    directory_path: Annotated[str, "要查询的目录系统完整路径"]
) -> Dict[str, Any]:
    """
    列出指定目录下所有直接子目录和文件的完整系统路径
    
    Args:
        directory_path: 要查询的目录完整路径
        
    Returns:
        包含子目录和文件完整路径信息的字典
        
    Raises:
        各种文件系统相关异常会被捕获并返回错误信息
    """
    try:
        # 验证路径是否存在
        if not os.path.exists(directory_path):
            return {
                "success": False,
                "error": f"目录不存在: {directory_path}",
                "directory": directory_path,
                "subdirectories": [],
                "files": [],
                "total_items": 0
            }
        
        # 验证是否为目录
        if not os.path.isdir(directory_path):
            return {
                "success": False,
                "error": f"指定路径不是目录: {directory_path}",
                "directory": directory_path,
                "subdirectories": [],
                "files": [],
                "total_items": 0
            }
        
        # 获取目录内容
        subdirectories = []
        files = []
        
        try:
            # 列出目录中的所有项目
            items = os.listdir(directory_path)
            
            for item in items:
                item_path = os.path.join(directory_path, item)
                absolute_path = os.path.abspath(item_path)
                
                if os.path.isdir(item_path):
                    subdirectories.append(absolute_path)
                elif os.path.isfile(item_path):
                    files.append(absolute_path)
                # 忽略其他类型的项目（如符号链接等）
                    
        except PermissionError:
            return {
                "success": False,
                "error": f"权限不足，无法访问目录: {directory_path}",
                "directory": directory_path,
                "subdirectories": [],
                "files": [],
                "total_items": 0
            }
        
        # 对结果进行排序，便于查看
        subdirectories.sort()
        files.sort()
        
        total_items = len(subdirectories) + len(files)
        
        logger.info(f"成功列出目录内容: {directory_path}, 共 {total_items} 个项目")
        
        return {
            "success": True,
            "directory": os.path.abspath(directory_path),
            "subdirectories": subdirectories,
            "files": files,
            "total_items": total_items
        }
        
    except Exception as e:
        error_msg = f"列出目录内容时发生未预期的错误: {str(e)}"
        logger.error(error_msg)
        return {
            "success": False,
            "error": error_msg,
            "directory": directory_path,
            "subdirectories": [],
            "files": [],
            "total_items": 0
        }
