import pydicom
from pydicom.dataset import Dataset, FileDataset
import datetime
import random

class DICOMManager:

    def generate_dicom(self, filename):

        file_meta = Dataset()

        ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b"\0"*128)

        ds.PatientName = "TestPatient"
        ds.PatientID = str(random.randint(1000,9999))
        ds.Modality = "CT"

        ds.ContentDate = str(datetime.date.today()).replace('-','')
        ds.ContentTime = str(datetime.datetime.now().time()).replace(':','')

        ds.save_as(filename)

        return filename