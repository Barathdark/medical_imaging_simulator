import random
import time

class DeviceSimulator:

    def __init__(self, pacs, dicom_manager):

        self.pacs = pacs
        self.dicom = dicom_manager

    def send_scan(self, index):

        filename = f"scan_{index}.dcm"

        dicom_file = self.dicom.generate_dicom(filename)

        duration = self.pacs.store_dicom(dicom_file)

        return duration