import os
import time
import logging

class PACSServer:

    def __init__(self, storage="data"):
        self.storage = storage
        os.makedirs(storage, exist_ok=True)

    def store_dicom(self, dicom_file):

        start = time.time()

        filename = os.path.basename(dicom_file)

        dest = os.path.join(self.storage, filename)

        with open(dicom_file, "rb") as src:
            with open(dest, "wb") as dst:
                dst.write(src.read())

        duration = time.time() - start

        logging.info(f"Stored {filename} in {duration}")

        return duration

    def retrieve_dicom(self, filename):

        start = time.time()

        path = os.path.join(self.storage, filename)

        with open(path, "rb") as f:
            data = f.read()

        duration = time.time() - start

        return data, duration