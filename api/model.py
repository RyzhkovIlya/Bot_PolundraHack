
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
        'q': text,
        'num': 1,
#        'safe': 'high',
        'fileType': 'jpg'}
#        'imgType': 'clipart|face|lineart|news|photo',
#        'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
#        'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow',
#        'imgColorType': 'color|gray|mono|trans',
#        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'}
    gis.search(search_params=_search_params)
        # take raw image data
    raw_image_data = random.choice(gis.results()).get_raw_data()
    return raw_image_data
# import os
# from google_images_search import GoogleImagesSearch
# from dotenv import load_dotenv
#
#
# def search_image(text: str) -> str:
#     load_dotenv()
#     GCS_DEVELOPER_KEY = os.getenv('TOKEN_GOOGLE')
#     GCS_CX = os.getenv('GOOGLE_CX')
#     gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
#     _search_params = {
#         'q': text,
#         'num': 10,
# #        'safe': 'high',
#         'fileType': 'jpg'}
# #        'imgType': 'clipart|face|lineart|news|photo',
# #        'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
# #        'imgDominantColor': 'black|blue|brown|gray|green|orange|pink|purple|red|teal|white|yellow',
# #        'imgColorType': 'color|gray|mono|trans',
# #        'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived'}
#     gis.search(search_params=_search_params)
#     for image in gis.results():
#         # take raw image data
#         raw_image_data = image.get_raw_data()
#         return raw_image_data
