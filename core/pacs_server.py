import os
import time

class PACSServer:

    def __init__(self, storage_path="data"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)

    def store_image(self, image_name, content):
        start = time.time()

        path = os.path.join(self.storage_path, image_name)

        with open(path, "w") as f:
            f.write(content)

        end = time.time()

        return end - start

    def retrieve_image(self, image_name):

        start = time.time()

        path = os.path.join(self.storage_path, image_name)

        with open(path) as f:
            data = f.read()

        end = time.time()

        return data, end - start