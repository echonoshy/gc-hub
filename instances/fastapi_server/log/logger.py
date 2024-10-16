from loguru import logger
import sys
import os

def setup_logger(log_name, log_dir, log_level="INFO"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{log_name}.log")

    # 移除所有现有的处理器
    logger.remove()

    # 添加控制台输出
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=log_level
    )

    # 添加文件输出
    logger.add(
        log_file,
        rotation="00:00",  # 每天午夜切分
        retention="7 days",  # 保留7天的日志文件
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} - {message}",
        compression="zip"  # 可以选择压缩旧日志
    )

    return logger

# 创建一个全局的logger实例
global_logger = setup_logger('CQA', 'logs')