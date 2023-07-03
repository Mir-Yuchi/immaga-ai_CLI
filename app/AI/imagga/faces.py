from .base import BaseImaggaManager


class ImaggaFaceDetectionsEndpoint(BaseImaggaManager):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret)
        self.FACE_DETECTIONS_BASE_URL = self.API_BASE_URL + '/faces/detections'

    def get_face_detection_data(self, img_url: str) -> dict | int:
        response = self.get(
            self.FACE_DETECTIONS_BASE_URL,
            params={
                'image_url': img_url,
                'return_face_id': True
            },
            headers=self.headers,
            auth=(self.api_key, self.api_secret)
        )
        if response.status_code == 200:
            return response.json()
        return response.status_code


def face_detection_runner(api_key: str, api_secret: str, image_url: str):
    face_detection_manager = ImaggaFaceDetectionsEndpoint(
        api_key,
        api_secret
    )
    code = face_detection_manager.get_face_detection_data(
        image_url
    )
    if isinstance(code, int):
        print('Не удалось получить инфу с картинки')
        return
    faces_obj = code['result']['faces']
    if not faces_obj:
        print('Чел, там нет морды')
        return
    percent = faces_obj[0]['confidence']
    print('В этой фотке на', str(percent) + '%', 'есть морда! Но чья морда - вообще хз')
