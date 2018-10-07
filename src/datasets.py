from zipfile import ZipFile
from io import BytesIO
from urllib.request import urlopen


DATASET_FOLDER = '../data/'
DATASET_URL_MAPPING = {
    'faces': 'https://download.pytorch.org/tutorial/faces.zip'
}


def fetch_dataset(name='faces'):

    url = DATASET_URL_MAPPING[name]

    resp = urlopen(url)

    with ZipFile(BytesIO(resp.read())) as my_zip_file:
        my_zip_file.extractall(DATASET_FOLDER)
