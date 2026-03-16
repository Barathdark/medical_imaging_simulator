import threading
import random
import string

class LoadSimulator:

    def __init__(self, pacs):
        self.pacs = pacs
        self.results = []

    def generate_fake_image(self):

        return ''.join(random.choices(string.ascii_letters, k=10000))

    def upload_task(self, i):

        image = self.generate_fake_image()

        filename = f"scan_{i}.dcm"

        time_taken = self.pacs.store_image(filename, image)

        self.results.append(time_taken)

    def simulate_load(self, num_images=50):

        threads = []

        for i in range(num_images):

            t = threading.Thread(target=self.upload_task, args=(i,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return self.results