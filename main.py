import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from detectemotion import detectemotion

import TeTe

def convert(ui):
    input = ui.lineEdit.text()
    result = detectemotion(input)['info']
    ui.lineEdit_2.setText(str(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = TeTe.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(convert,ui))
    sys.exit(app.exec_())

