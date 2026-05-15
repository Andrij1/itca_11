import sys
from PySide6.QtWidgets import QApplication
# QtWidgets - submodule for all GUI widget classes (windows, buttons from the framework)
# QApplication - runs the app, creates GUI context, manages event loop, engine of the app
from gui.mainwindow import MainWindow
# all the app main window - display screen, buttons, layout
# connects buttons-clicks, processes inputs, handle calc-s, updates display
# press “7” → adds "7" to display, “+” → stores operation, “=” → computes result

def main():
    app = QApplication(sys.argv)    # app - QApplication instance, __init__ ialized
                                    # utilizes system arguments, like scommands to run, debu app etc.
                                    # ex. python app.py --style Fusion, sys.argv = ["app.py", "--debug", "--style", "Fusion"]
    window = MainWindow()           # creates the real calculator working class objects in the class instacne
                                    # its buttons, inputs, calculation calls etc.
                                    # MainWindow is there created from QMainWIndow
    window.show()                   # QWidget.show() - displays the widget (draw the window, display UI)
                                    # inherits from QMainindow (show, hide, resize), GUI, events, main window
    sys.exit(app.exec())            # run the app until closed, finish smoothly with status code


if __name__ == "__main__":
    main()