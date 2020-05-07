import yaml
import pathlib  

def get_config():
    try:
        # Windows open
        with open(f"{pathlib.Path().cwd()}\\utils\\config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)
            return cfg
    except:
        # Linux open
        with open(f"{pathlib.Path().cwd()}/utils/config.yml", "r") as ymlfile:
            cfg = yaml.safe_load(ymlfile)
            return cfg

CONFIG = get_config()

def print_config(c=CONFIG):
    for v in c:
        print(v)