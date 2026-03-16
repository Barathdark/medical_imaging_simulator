from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout

class Dashboard(QWidget):

    def __init__(self, controller):

        super().__init__()

        self.controller = controller

        self.label = QLabel("Medical Imaging Load Simulator")

        self.button = QPushButton("Start Simulation")

        self.button.clicked.connect(self.run_test)

        layout = QVBoxLayout()

        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def run_test(self):

        metrics = self.controller.run_simulation()

        self.label.setText(str(metrics))