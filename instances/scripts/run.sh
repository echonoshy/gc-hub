#!/bin/bash

# 读取配置
HOST=$(python config/read_config_cli.py server.host)
PORT=$(python config/read_config_cli server.port)
WORKERS=$(python config/read_config_cli app.workers)
RELOAD=$(python config/read_config_cli app.reload)

# 将 RELOAD 转换为相应的命令行参数
if [ "$RELOAD" = "true" ]; then
  RELOAD_FLAG="--reload"
else
  RELOAD_FLAG=""
fi

# 启动 FastAPI 服务
echo "Starting FastAPI service on $HOST:$PORT with $WORKERS workers..."

uvicorn main:app --host $HOST --port $PORT --workers $WORKERS $RELOAD_FLAG &

echo "FastAPI service is running on http://$HOST:$PORT"
