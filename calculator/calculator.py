import sys
from PySide6.QtWidgets import QApplication
from gui.mainwindow import MainWindow


def main():
    """
    Create and run the calculator application.
    Initializes the QApplication instance, creates the main window,
    displays it, and starts the Qt event loop.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()