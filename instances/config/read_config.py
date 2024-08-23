from omegaconf import OmegaConf

class Config:
    _config = None

    @classmethod
    def load_config(cls, file_path):
        if cls._config is None:
            cls._config = OmegaConf.load(file_path)
        return cls._config

# 在程序启动时加载配置文件
CONFIG = Config.load_config('path/to/conf.yml')

