import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from functools import partial
from detectemotion import detectemotion
from musicreco import musicreco
from loadqs import QSSLoader

import TeTe

def convert(ui):
    input = ui.lineEdit.text()
    emotionresult = detectemotion(input)
    musicresult = musicreco(emotionresult)

    ui.lineEdit_2.setText(emotionresult['info'])
    ui.listWidget.clear()
    ui.listWidget.addItems(musicresult[1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow() 
    ui = TeTe.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Music & Emotion Predictions")
    MainWindow.setStyleSheet("#MainWindow{border-image:url(6891668886439_.pic.jpg)}")
    ui.lineEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
    ui.lineEdit_2.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
    ui.listWidget.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
    ui.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0.6);")
    
    # style_file = './style.qss'
    # style_sheet = QSSLoader.read_qss_file(style_file)
    # MainWindow.setStyleSheet(style_sheet)

    MainWindow.show()
    ui.pushButton.clicked.connect(partial(convert,ui))

    sys.exit(app.exec_())

