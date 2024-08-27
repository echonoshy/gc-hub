#!/bin/bash

# 读取配置
HOST=$(python config/read_config_cli.py server.host)
PORT=$(python config/read_config_cli server.port)
WORKERS=$(python config/read_config_cli app.workers)


# 启动 FastAPI 服务
echo "Starting FastAPI service on $HOST:$PORT with $WORKERS workers..."

nohup uvicorn main:app --host $HOST --port $PORT --workers $WORKERS &

echo "FastAPI service is running on http://$HOST:$PORT"
