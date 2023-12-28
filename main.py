import sys
from PyQt5.QtWidgets import *

from node_editor_wnd import NodeEditorWnd

if __name__ == '__main__':
    # print("Hello World")
    app = QApplication(sys.argv);

    wnd = NodeEditorWnd();

    sys.exit(app.exec_());