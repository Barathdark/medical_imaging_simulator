from concurrent.futures import ThreadPoolExecutor

class LoadEngine:

    def __init__(self, device):

        self.device = device

    def run_load(self, count=100):

        results = []

        def task(i):
            return self.device.send_scan(i)

        with ThreadPoolExecutor(max_workers=20) as executor:

            for r in executor.map(task, range(count)):
                results.append(r)

        return results