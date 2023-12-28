import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    # print("Hello World")
    app = QApplication(sys.argv);

    label = QLabel("Hello , PyQt5 !");
    label.show();

    sys.exit(app.exec_());