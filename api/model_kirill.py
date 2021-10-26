import os
from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv


def search_image(text: str) -> str:
    load_dotenv()
    GCS_DEVELOPER_KEY = os.getenv('GOOGLE_TOKEN')
    GCS_CX = os.getenv('GOOGLE_CX')
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    _search_params = {
        'q': text,
        'num': 10,
        'fileType': 'jpg'}
    gis.search(search_params=_search_params)
    for image in gis.results():
        raw_image_data = image.get_raw_data()
        return raw_image_data