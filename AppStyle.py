from PyQt5.QtGui import QFont



class AppStyle:

    style_name = 'Default'

    class MainWindow:
        title = 'CatBoots'
        style = """QMainWindow{
                background: rgb(170,170,170);
            }
            """


    class Font:
        title = QFont()

        instrument = QFont('Kanit', 20)
    

    class Label:
        instrument = """QLabel{
                border-radius: 3px;
            }
            """
    

    class Button:
        beat = """QPushButton{
                background: #D5FCD3;
                border-radius: 5px;
            }
            QPushButton:hover{
                border: 2px solid rgb(30,30,30);
                border-radius: 5px;
            }
            QPushButton:checked{
                background: #48FF28;
                border-radius: 5px;
            }
            """