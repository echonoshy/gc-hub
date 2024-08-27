import logging
import logging.handlers
import socket
import os
from datetime import datetime
from functools import wraps


def singleton(func):
    instances = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in instances:
            instances[key] = func(*args, **kwargs)
        return instances[key]

    return wrapper


@singleton
# 配置日志记录器
def setup_logger(log_directory="logs", log_level="INFO"):
    # 获取当前日期和主机名
    hostname = socket.gethostname()
    current_date = datetime.now().strftime("%Y-%m-%d")

    # 日志文件路径
    log_directory = log_directory
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_filename = f"{log_directory}/{hostname}-{current_date}.log"

    # 创建日志记录器
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # 创建文件处理器，按天进行切分
    file_handler = logging.handlers.TimedRotatingFileHandler(
        log_filename, when='midnight', interval=1, backupCount=7
    )
    file_handler.setLevel(log_level)

    # 创建终端处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # 定义日志输出格式
    formatter = logging.Formatter(
        '[%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d pid:%(process)d] %(message)s'
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


if __name__ == "__main__":
    # 使用日志记录器
    logger = setup_logger()

    # 记录日志示例
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
