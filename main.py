import sys

from PyQt5.QtWidgets import QApplication

from core.pacs_server import PACSServer
from core.dicom_manager import DICOMManager
from simulator.device_simulator import DeviceSimulator
from simulator.load_engine import LoadEngine
from analytics.metrics_engine import MetricsEngine
from analytics.report_generator import ReportGenerator
from ui.dashboard import Dashboard


class Controller:

    def run_simulation(self):

        pacs = PACSServer()

        dicom = DICOMManager()

        device = DeviceSimulator(pacs, dicom)

        engine = LoadEngine(device)

        results = engine.run_load(200)

        metrics_engine = MetricsEngine()

        metrics, df = metrics_engine.compute(results)

        report = ReportGenerator()

        report.generate(metrics)

        return metrics


app = QApplication(sys.argv)

controller = Controller()

window = Dashboard(controller)

window.show()

sys.exit(app.exec_())