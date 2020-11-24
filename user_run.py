import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget

from GUI import Ui_Form
from data_dealer import run


class MyMainFrom(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.left_close.clicked.connect(self.close)
        self.left_mini.clicked.connect(self.slot_max_or_recv)
        self.left_visit.clicked.connect(self.showMinimized)
        self.produce.clicked.connect(self.display)

    def slot_max_or_recv(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def display(self):
        orientation = self.orientation.text()
        destination = self.destination.text()
        res = run(file_path='BaseSubWayInfo.txt', subwayStationNum=0, subwayIndex=0, subwayDict={},
                  reverseSubwayDict={}, D=[], orientation=orientation, destination=destination)
        self.output.setText(str(res))


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    myWin = MyMainFrom()
    myWin.show()
    sys.exit(app.exec_())
