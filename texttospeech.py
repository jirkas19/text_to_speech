#epub to txt
#bere jen p tag
#je nutne nainstalovat knihovny pyttsx3, PyQt5



import sys
import pyttsx3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Konverter(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.setFixedHeight(200)
        self.setFixedWidth(500)
        self.soubor=QtWidgets.QLabel("umisteni souboru")
        self.tacitko_konce = QtWidgets.QPushButton('konec')
        self.tacitko_konce.clicked.connect(self.close)
        self.tlacitko_soubor = QtWidgets.QPushButton('otevri')
        self.tlacitko_soubor.clicked.connect(self.otevri)
        self.tlacitko_audio = QtWidgets.QPushButton('uloz')
        self.tlacitko_audio.clicked.connect(self.uloz)
        p = QtWidgets.QGridLayout()
        p.addWidget(self.soubor, 0,0)
        p.addWidget(self.tlacitko_soubor, 1,0)
        p.addWidget(self.tlacitko_audio, 2,0)
        p.addWidget(self.tacitko_konce, 3, 0)
        self.setLayout(p)
        self.show()

    def otevri(self):
        otevri=QFileDialog.getOpenFileName(self, "otevri","",'(*.txt *.doc *.docx)')
        if len(str(otevri))>=9:
            c=str(otevri)[2:-26]
            print(c)


    def uloz(self):
        uloz=QFileDialog.getSaveFileName(self,"uloz","knizka.txt","(*.txt)")




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = Konverter(windowTitle='konverter')
    sys.exit(app.exec_())
