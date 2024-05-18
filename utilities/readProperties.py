import configparser

config = configparser.RawConfigParser()
config.read(".//configs//config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url
