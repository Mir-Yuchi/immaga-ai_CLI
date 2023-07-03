from .base import BaseImaggaManager


class ImaggaTagsEndpoint(BaseImaggaManager):

    def __init__(self, api_key: str, api_secret: str, lang: str = 'ru') -> None:
        super().__init__(api_key, api_secret)
        self.API_TAGS_BASE_URL = self.API_BASE_URL + '/tags'
        self.lang = lang

    def get_photo_tags(self, photo_url: str) -> dict | int:
        response = self.get(
            self.API_TAGS_BASE_URL,
            params={
                'image_url': photo_url,
                'language': self.lang,
            },
            headers=self.headers,
            auth=(self.api_key, self.api_secret)
        )
        if response.status_code == 200:
            return response.json()
        return response.status_code


def tags_runner(api_key: str, api_secret: str, image_url: str):
    tags_manager = ImaggaTagsEndpoint(
        api_key,
        api_secret
    )
    tags_response = tags_manager.get_photo_tags(
        image_url
    )
    if isinstance(tags_response, int):
        print('Ошибка! Код ошибки', tags_response)
        return
    tags_list = tags_response['result']['tags']
    tags_dict = {}
    for tag_obj in tags_list:
        tags_dict[tag_obj['confidence']] = tag_obj['tag']['ru']
    percent, obj = list(tags_dict.items())[0]
    print(
        'Найденный элемент с вероятностью',
        percent.__str__() + '%', 'совпадает с', obj
    )
