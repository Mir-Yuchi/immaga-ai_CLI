from .base import BaseImaggaManager


class ImaggaColorsEndpoint(BaseImaggaManager):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret)
        self.API_COLORS_BASE_URL = self.API_BASE_URL + '/colors'

    def get_colors_data(self, img_url: str) -> dict | int:
        response = self.get(
            self.API_COLORS_BASE_URL,
            params={
                'image_url': img_url
            },
            headers=self.headers,
            auth=(self.api_key, self.api_secret)
        )
        if response.status_code == 200:
            return response.json()
        return response.status_code


def colors_runner(api_key: str, api_secret: str, image_url: str):
    colors_managers = ImaggaColorsEndpoint(
        api_key,
        api_secret
    )
    code = colors_managers.get_colors_data(
        image_url
    )
    if isinstance(code, int):
        print('Не удалось получить инфу с картинки')
        return
    colors_obj = code['result']['colors']
    background_colors = colors_obj['background_colors']
    foreground_colors = colors_obj['foreground_colors']
    print('Фоновые цвета:')
    for color in background_colors:
        print(color['html_code'])
    print('НЕ Фоновые цвета:')
    for color in foreground_colors:
        print(color['html_code'])
