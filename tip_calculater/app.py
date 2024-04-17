import sys

from PyQt6.QtWidgets import (
    QGridLayout,
    QApplication,
    QDoubleSpinBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QGridLayout()

        self.money_spent_input = QDoubleSpinBox()
        self.money_spent_input.setPrefix("$ ")
        self.money_spent_input.setMinimum(0.0)

        self.tip_percent_input = QSpinBox()
        self.tip_percent_input.setSuffix("%")
        self.tip_percent_input.setMinimum(0)

        calculate_button = QPushButton("Calculate!")

        instructions_text = QTextEdit("Instructions")

        tip_amount_output = QLabel("Tip Amount")

        total_spent_output = QLabel("Total Spent")

        #Add widgits to the grid
        layout.addWidget(self.money_spent_input, 0,0)
        layout.addWidget(instructions_text, 0,1,2,2)
        layout.addWidget(self.tip_percent_input, 1,0)
        layout.addWidget(calculate_button, 2,0)
        layout.addWidget(tip_amount_output, 2,1)
        layout.addWidget(total_spent_output, 2,2)


        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()