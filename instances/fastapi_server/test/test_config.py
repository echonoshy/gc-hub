import sys
import os 

# 手动更新PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'instances/fastapi_server')))


def test_config():
    from config import CONFIG
    assert CONFIG.database.port == 3306
    
def test_cli():
    import subprocess

    bash_script = """
        cd instances/fastapi_server
        python config/read_config_cli.py database.port
    """
    
    # 执行 Bash 命令并获取输出
    process = subprocess.Popen(bash_script, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # assert stderr == ""
    assert int(stdout) == 3306      # b'3306/n'

        