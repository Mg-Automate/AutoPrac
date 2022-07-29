import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL(self):
        url = config.get('common data','pravid_login_url')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common data','username')
        return username

    @staticmethod
    def getPassword():
        pasword = config.get('common data','password')
        return pasword



