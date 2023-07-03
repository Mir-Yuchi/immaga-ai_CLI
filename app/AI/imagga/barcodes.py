from .base import BaseImaggaManager


class ImaggaBarcodesEndpoint(BaseImaggaManager):

    def __init__(self, api_key: str, api_secret: str) -> None:
        super().__init__(api_key, api_secret)
        self.API_BARCODES_BASE_URL = self.API_BASE_URL + '/barcodes'

    def get_barcode_data(self, barcode_img_url: str) -> dict | int:
        response = self.get(
            self.API_BARCODES_BASE_URL,
            params={
                'image_url': barcode_img_url
            },
            headers=self.headers,
            auth=(self.api_key, self.api_secret)
        )
        if response.status_code == 200:
            return response.json()
        return response.status_code


def barcode_runner(api_key: str, api_secret: str, image_url: str):
    barcodes_manager = ImaggaBarcodesEndpoint(
        api_key,
        api_secret
    )
    code = barcodes_manager.get_barcode_data(image_url)
    if isinstance(code, int):
        print('Не удалось получить инфу с картинки')
        return
    data = code['result']['barcodes'][0]['data']
    print('Данные штрихкода:', data)
