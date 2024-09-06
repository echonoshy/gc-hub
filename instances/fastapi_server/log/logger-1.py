from loguru import logger
import os

def setup_logger(log_name, log_dir, log_level="INFO"):
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, f"{log_name}.log")

    # 配置 loguru 日志器
    logger.add(
        log_file,
        rotation="00:00",  # 每天午夜切分
        retention="7 days",  # 保留7天的日志文件
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        compression="zip"  # 可以选择压缩旧日志
    )

    return logger


# 使用示例
log = setup_logger('CQA', 'logs')

log.debug("This is a test log message.")
log.info("This is a test log message.")
log.warning("This is a test log message.")
log.error("This is a test log message.")
