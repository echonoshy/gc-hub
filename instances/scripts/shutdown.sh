#!/bin/bash

# 获取 FastAPI 服务的 PID
PID=$(ps aux | grep '[u]vicorn' | awk '{print $2}')

# 如果找到进程 ID, 则终止进程
if [ -n "$PID" ]; then
  echo "Shutting down FastAPI service with PID: $PID"
  kill $PID

  # 等待进程终止
  wait $PID
  echo "FastAPI service has been shut down."
else
  echo "FastAPI service is not running."
fi
