from utilities.logger import LogGen
from utilities.readProperties import ReadConfig


class BaseTest:
    baseURL = ReadConfig.get_application_url()
    logger = LogGen.log_gen()
