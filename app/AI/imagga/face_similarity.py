from .base import BaseImaggaManager
from .faces import ImaggaFaceDetectionsEndpoint


class ImaggaFaceSimilarityEndpoint(BaseImaggaManager):

    def __init__(self, api_key: str, api_secret: str):
        super().__init__(api_key, api_secret)
        self.FACE_SIMILARITY_BASE_URL = self.API_BASE_URL + '/faces/similarity'

    def get_face_similarity_data(self, face_id: str, second_face_id: str) -> dict | int:
        response = self.get(
            self.FACE_SIMILARITY_BASE_URL,
            params={
                'face_id': face_id,
                'second_face_id': second_face_id
            },
            headers=self.headers,
            auth=(self.api_key, self.api_secret)
        )
        if response.status_code == 200:
            return response.json()
        return response.status_code


def face_similarity_runner(api_key: str, api_secret: str, image_url: str):
    second_face_photo_url = input('Ссылка на фотку второй морды: ')
    face_detection_manager = ImaggaFaceDetectionsEndpoint(
        api_key,
        api_secret
    )
    face_ids = []
    for url in image_url, second_face_photo_url:
        code = face_detection_manager.get_face_detection_data(url)
        if isinstance(code, int):
            print('По фотке', url, 'не удалось получить инфу')
            return
        faces_obj = code['result']['faces']
        if not faces_obj:
            print('На фотке', url, 'морды не обнаружено!')
            return
        face_ids.append(faces_obj[0]['face_id'])
    similarity_endpoint = ImaggaFaceSimilarityEndpoint(
        api_key,
        api_secret
    )
    response = similarity_endpoint.get_face_similarity_data(
        *face_ids
    )
    if isinstance(response, int):
        print('Не удалось проверить морды')
        return
    percent = response['result']['score']
    print('Обе морды похожи друг на друга на', str(percent) + '%')
