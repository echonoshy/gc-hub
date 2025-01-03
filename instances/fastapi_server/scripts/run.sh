#!/bin/bash

# 读取配置
HOST=$(python config/read_config_cli.py server.host)
PORT=$(python config/read_config_cli server.port)
WORKERS=$(python config/read_config_cli app.workers)


# 启动 FastAPI 服务
echo "Starting FastAPI service on $HOST:$PORT with $WORKERS workers..."

# 使用uvicorn启动
# nohup uvicorn main:app --host $HOST --port $PORT --workers $WORKERS &

# gunicorn 启动更稳定
# logger已经将stdout 输出到logger file
nohup gunicorn main:app \
  --bind "$HOST:$PORT" \
  --workers $WORKERS \
  --worker-class "uvicorn.workers.UvicornWorker" \
  > /dev/null &


echo "FastAPI service is running on http://$HOST:$PORT"
