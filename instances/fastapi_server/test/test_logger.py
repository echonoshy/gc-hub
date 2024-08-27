import sys
import os 

# 手动更新PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'instances/fastapi_server')))


def test_logger():
    import logging 
    from log import logger
    logger = logger.setup_logger(log_level="INFO")
    
    assert logger.level == logging.INFO 