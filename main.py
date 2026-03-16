import sys

from PyQt5.QtWidgets import QApplication

from core.pacs_server import PACSServer
from simulator.load_simulator import LoadSimulator
from analytics.performance_analyzer import PerformanceAnalyzer
from analytics.report_generator import ReportGenerator
from ui.dashboard import Dashboard


class Controller:

    def run_simulation(self):

        pacs = PACSServer()

        simulator = LoadSimulator(pacs)

        results = simulator.simulate_load(100)

        analyzer = PerformanceAnalyzer()

        metrics, df = analyzer.analyze(results)

        report = ReportGenerator()

        report.generate(metrics)

        return metrics


app = QApplication(sys.argv)

controller = Controller()

window = Dashboard(controller)

window.show()

sys.exit(app.exec_())