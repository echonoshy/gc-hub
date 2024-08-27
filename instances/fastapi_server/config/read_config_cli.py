import sys
from omegaconf import OmegaConf

def read_config(key):
    config = OmegaConf.load('config/conf.yml')
    
    keys = key.split('.')
    value = config
    for k in keys:
        value = value.get(k)
        if value is None:
            break
    return value

if __name__ == "__main__":
    key = sys.argv[1]
    value = read_config(key)
    if value is not None:
        print(value)
