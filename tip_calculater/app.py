import sys
import Controller

from PyQt6.QtWidgets import (
    QGridLayout,
    QApplication,
    QDoubleSpinBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QSpinBox,
    QTextEdit,
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
        self.money_spent_input.setMaximum(999999999.99)

        self.tip_percent_input = QSpinBox()
        self.tip_percent_input.setSuffix("%")
        self.tip_percent_input.setMinimum(0)
        self.tip_percent_input.setMaximum(100)

        self.calculate_button = QPushButton("Calculate!")
        #Add a calculate function
        self.calculate_button.clicked.connect(self.calculate_tip)

        self.instructions_text = QTextEdit("Instructions")

        self.tip_amount_output = QLabel("Tip Amount")
        self.tip_amount_output.setContentsMargins(25, 0, 25, 0)

        self.total_spent_output = QLabel("Total Spent")
        self.total_spent_output.setContentsMargins(25, 0, 25, 0)

        #Add widgits to the grid
        layout.addWidget(self.money_spent_input, 0,0)
        layout.addWidget(self.instructions_text, 0,1,2,2)
        layout.addWidget(self.tip_percent_input, 1,0)
        layout.addWidget(self.calculate_button, 2,0)
        layout.addWidget(self.tip_amount_output, 2,1)
        layout.addWidget(self.total_spent_output, 2,2)


        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
    
    def calculate_tip(self):
        money_spent = self.money_spent_input.value()
        tip_percent = self.tip_percent_input.value()
        tip = Controller.get_tip(money_spent, tip_percent)
        total = Controller.get_total(money_spent, tip)
        tip = f"${tip}"
        total = f"${total}"
        self.tip_amount_output.setText(tip)
        self.total_spent_output.setText(total)

app = QApplication(sys.argv)
stylesheet = None
styles_path = "Resorces/Styles.qss"
#gets the code from the style sheet
with open(styles_path, "r") as f:
    stylesheet = f.read() 
app.setStyleSheet(stylesheet)
window = MainWindow()
window.show()

app.exec()