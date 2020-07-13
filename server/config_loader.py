import configparser
import os

config = configparser.ConfigParser()
config.read("server/config.ini")


def add_app_configs(cinfigs: dict):
    for key, val in cinfigs.items():
        if os.environ.get(key) is None:
            os.environ.setdefault(key, val)


def load_config():
    print("loading Config ......")
    current_configs = dict()
    for sec in config.sections():
        current_configs.update(config.items(sec))

    add_app_configs(current_configs)
    print('Config Loaded.....')
