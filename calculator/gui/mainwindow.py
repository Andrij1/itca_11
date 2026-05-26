from PySide6.QtWidgets import QMainWindow
from .ui_mainwindow import Ui_MainWindow        # ready-made app framework
from src.calc import Calculator

class MainWindow(QMainWindow):
    """
    Main calculator window.
    Handles GUI initialization, button signal connections,
    and communication between the user interface and
    calculator logic.
    """

    def __init__(self):
        """
        Initialize the main window and connect UI events.
        Sets up the generated Qt interface, creates the
        Calculator instance, and connects button signals
        to their corresponding handlers.
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.calc = Calculator()
        btns_nums = [
            'BTN_0', 'BTN_1', 'BTN_2', 'BTN_3', 'BTN_4',
            'BTN_5', 'BTN_6', 'BTN_7', 'BTN_8', 'BTN_9',
        ]

        btns_ops = {
            "BTN_10" : "%",
            "BTN_11": "√",
            "BTN_12" : "+",
            "BTN_13": "-",
            "BTN_14": "/",
            "BTN_15": "*"
        }

        for idx, btn_name in enumerate(btns_nums):
            btn = getattr(self.ui, btn_name)
            btn.clicked.connect(lambda checked=False, x=idx: self.on_button(x))

        for name, sym in btns_ops.items():
            btn = getattr(self.ui, name)
            btn.clicked.connect(lambda checked=False, x=sym: self.on_operator(x))

        self.ui.BTN_16.clicked.connect(self.on_calc)
        self.ui.BTN_C.clicked.connect(self.on_clear_all)
        self.ui.BTN_PT.clicked.connect(self.on_point)         # !!!
        self.ui.BTN_X.clicked.connect(self.on_clear_last)


    def on_button(self, value):
        """
        Handle numeric button input.
        Updates the display and passes the entered
        number to the calculator logic.
        Args:
            value (int): The digit entered by the user.
        """
        self.ui.Display.setText(self.ui.Display.text() + str(value))
        self.calc.set_variable(value)


    def on_operator(self, value):
        """
        Handle operator button input.
        Sends the selected operator to the calculator
        and updates the display.
        Args:
            value (str): The selected operator symbol.
        """
        self.ui.Display.setText(str(value))
        self.calc.set_operator(str(value))


    def on_point(self, value):
        """
        Handle decimal point input.
        Adds a decimal point to the current number
        and updates the display.
        """
        self.calc.set_point(self.ui.BTN_PT.text())
        self.ui.Display.setText(self.calc.collected)


    def on_clear_last(self):
        """
        Remove the last entered value or operator.
        Updates both the calculator state and display.
        """
        self.calc.clear_last_variable()
        self.ui.Display.setText(self.calc.operator)


    def on_clear_all(self):
        """
        Clear the calculator state and display.
        Resets all stored input and results.
        """
        self.ui.Display.setText('')
        self.calc.clear()


    def on_calc(self):
        """
        Evaluate the current expression.
        Calculates the result and displays the output.
        """
        result = self.calc.calculate()
        self.ui.Display.setText(str(result))