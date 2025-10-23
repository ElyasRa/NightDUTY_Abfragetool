import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton
# Include other necessary imports...

# Stylesheets
STYLESHEET = "/* Your stylesheet here */"
PANNE_STYLESHEET = "/* Your panne stylesheet here */"
OELSPUR_STYLESHEET = "/* Your oelspur stylesheet here */"
MOBI_STYLESHEET = "/* Your mobi stylesheet here */"
KILIAN_STYLESHEET = "/* Your kilian stylesheet here */"
RUDOLPH_STYLESHEET = "/* Your rudolph stylesheet here */"
WEHNER_STYLESHEET = "/* Your wehner stylesheet here */"

class PasswordDialog(QDialog):
    def __init__(self):
        super().__init__()
        # Initialize dialog...

class WehnerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class RudolphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class KilianWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        report_button = QPushButton("Report Einsatzzentrale Data", self)
        report_button.clicked.connect(self.report_einsatzzentrale_data)
        # Initialize UI...

    def report_einsatzzentrale_data(self):
        # Logic to generate tab-separated 2-row Excel format data...
        pass

    def report_gdv_bayern_data(self):
        # Logic for GDV Bayern report...
        pass

    def report_bus_lkw_data(self):
        # Logic for Bus LKW report...
        pass

class MobiWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class OelspurWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class PanneUnfallWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class ContentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize window...

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize main window...

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())