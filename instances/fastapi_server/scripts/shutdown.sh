#!/bin/bash

# 读取配置
PORT=$(python config/read_config_cli server.port)

# 查找占用指定端口的所有进程 ID
PIDS=$(lsof -t -i:$PORT)

# 判断是否找到进程 ID
if [ -z "$PIDS" ]; then
  echo "No process found running on port $PORT"
else
  # 终止所有找到的进程
  lsof -t -i:$PORT | xargs kill -9
  echo "All FastAPI services running on port $PORT have been stopped."
fi
