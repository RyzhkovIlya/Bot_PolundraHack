import os
from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import random

def picture(text: str) -> str:
    load_dotenv()
    GCS_DEVELOPER_KEY = os.getenv('TOKEN_GOOGLE')
    GCS_CX = os.getenv('GOOGLE_CX')
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    _search_params = {
        'q': text+' mem',
        'num': 10,
        'fileType': 'jpg'}

    gis.search(search_params=_search_params)
    return random.choice(gis.results()).get_raw_data()

