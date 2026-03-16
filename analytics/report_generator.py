import os
from openpyxl import Workbook

class ReportGenerator:

    def generate(self, metrics):

        os.makedirs("reports", exist_ok=True)

        wb = Workbook()
        sheet = wb.active

        sheet.append(["Metric","Value"])

        for k,v in metrics.items():
            sheet.append([k,v])

        wb.save("reports/performance.xlsx")