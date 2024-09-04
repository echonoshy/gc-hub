#!/bin/bash

# 读取配置
PORT=$(python config/read_config_cli server.port)

# 查找占用指定端口的所有进程 ID
PIDS=$(lsof -t -i:$PORT)

# 判断是否找到进程 ID
if [ -z "$PIDS" ]; then
  echo "No process found running on port $PORT"
else
  # 逐个终止所有找到的进程
  for PID in $PIDS; do
    kill -9 $PID
    echo "Terminated process with PID $PID."
  done
  echo "All FastAPI services running on port $PORT have been stopped."
fi
