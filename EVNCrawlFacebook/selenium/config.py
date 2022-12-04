from os.path import exists
import yaml

CONFIG_PATH = "EVNCrawlFacebook/selenium/config.yml"


class Config:
    def __init__(self) -> None:
        self.USERNAME: str = ''
        self.PASSWORD: str = ''


def get_config() -> Config:
    if not exists(CONFIG_PATH):
        raise Exception('Please check the path of config.yml!')
    else:
        with open(CONFIG_PATH, 'r') as file:
            yaml_config = yaml.safe_load(file)
            config = Config()
            config.__dict__.update(yaml_config)
            return config
