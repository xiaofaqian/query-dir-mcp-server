#!/usr/bin/env python3
"""
Excel MCP Server using FastMCP
"""

import logging
from mcp.server.fastmcp import FastMCP

# 导入工具模块
from tools import list_directory_contents

# Configure logging for comprehensive error tracking
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mcp-server")

# Create FastMCP server instance
mcp = FastMCP("query-dir-mcp-server")

# 注册工具
mcp.tool()(list_directory_contents)


if __name__ == "__main__":
    logger.info("[Setup] Initializing MCP Server...")
    mcp.run()
