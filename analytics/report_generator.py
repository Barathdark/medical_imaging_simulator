from openpyxl import Workbook

class ReportGenerator:

    def generate(self, metrics):

        wb = Workbook()
        sheet = wb.active

        sheet.append(["Metric", "Value"])

        for k,v in metrics.items():
            sheet.append([k, v])

        wb.save("reports/performance_report.xlsx")