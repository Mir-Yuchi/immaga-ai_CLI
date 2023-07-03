from requests import Session


class BaseImaggaManager(Session):
    API_BASE_URL = 'https://api.imagga.com/v2'
    headers = {
        'User-Agent': 'I\'m Fake user-agent',
    }

    def __init__(self, api_key: str, api_secret: str):
        super().__init__()
        self.__api_key = api_key
        self.__api_secret = api_secret

    @property
    def api_key(self):
        return self.__api_key

    @property
    def api_secret(self):
        return self.__api_secret
