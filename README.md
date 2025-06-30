# Query Directory MCP Server

一个基于 FastMCP 的 Model Context Protocol (MCP) 服务器，提供目录查询功能。

## 功能特性

### list_directory_contents 工具

根据指定的系统完整目录路径，列出该目录下所有直接子目录和文件的完整系统路径（不递归遍历）。

**功能特点：**
- 列出指定目录下的所有子目录和文件
- 返回完整的系统路径
- 不进行递归遍历，只查询直接子项
- 完善的错误处理机制
- 支持权限检查和路径验证

**返回数据格式：**
```json
{
    "success": true,
    "directory": "查询的目录路径",
    "subdirectories": ["子目录1完整路径", "子目录2完整路径"],
    "files": ["文件1完整路径", "文件2完整路径"],
    "total_items": 总项目数量
}
```

## 项目结构

```
query-dir-mcp-server/
├── server.py              # 主服务器文件
├── tools/                 # 工具模块目录
│   ├── __init__.py        # 模块初始化文件
│   └── list_directory_contents.py  # 目录查询工具
└── README.md              # 项目说明文档
```

## 安装和使用

### 依赖要求

- Python 3.8+
- FastMCP
- typing-extensions

### 安装依赖

```bash
pip install fastmcp typing-extensions
```

### 运行服务器

```bash
python server.py
```

## 开发规范

本项目遵循以下开发规范：

### 工具开发规范
- 所有工具方法使用三引号包裹方法描述
- 使用 `Annotated` 类型注解规范化参数
- 实现严格的异常处理机制
- 遵循 Python PEP 8 编码规范

### 文件组织规范
- 每个 MCP 工具放在独立文件中
- 所有工具文件放在 `tools/` 目录下
- 工具方法名与文件名保持一致
- 使用 snake_case 命名约定

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目。
