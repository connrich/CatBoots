from BeatMaker import BeatMaker
from PyQt5.QtWidgets import QApplication, QMainWindow
from AppStyle import AppStyle
import sys



class CatBoots(QMainWindow):
    def __init__(self, style=AppStyle):
        super().__init__()
        self.setWindowTitle(style.MainWindow.title)
        self.setStyleSheet(style.MainWindow.style)

        self.BeatMaker = BeatMaker(self, style=style)
        self.setCentralWidget(self.BeatMaker)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = CatBoots()
    MainWindow.show()
    sys.exit(app.exec())