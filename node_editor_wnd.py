from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from node_scene import Scene
from node_node import Node
from node_socket import Socket
from node_graphics_view import QDMGraphicsView

class NodeEditorWnd(QWidget):
    def __init__(self,parent = None):
        super().__init__(parent);

        self.stylesheet_filename = 'qss/nodestyle.qss';
        self.loadStylesheet(self.stylesheet_filename);

        self.initUI();

    def initUI(self):
        self.setGeometry(200,200,800,600); #x-offset, y-offset,window-width , window-height

        self.layout = QVBoxLayout();
        self.layout.setContentsMargins(0,0,0,0);
        self.setLayout(self.layout);


        # create graphics scene
        self.scene = Scene();
        #self.grScene = self.scene.grScene;

        node = Node(self.scene, "My Awesome Node", inputs=[1,2,3], outputs=[1])

        # create graphics view
        self.view = QDMGraphicsView(self.scene.grScene,self);
        self.layout.addWidget(self.view);


        self.setWindowTitle("Node Editor");
        self.show();


        # self.addDebugContent();

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green);
        outllinePen = QPen(Qt.black);
        outllinePen.setWidth(2);

        rect = self.grScene.addRect(-100,-100,80,100,outllinePen,greenBrush);
        rect.setFlag(QGraphicsItem.ItemIsMovable);

        text = self.grScene.addText("This is my awesome text!");
        text.setFlag(QGraphicsItem.ItemIsSelectable);
        text.setFlag(QGraphicsItem.ItemIsMovable);
        text.setDefaultTextColor(QColor.fromRgbF(1.0,1.0,1.0));

        widget1 = QPushButton("Hello World");
        proxy1 = self.grScene.addWidget(widget1);
        proxy1.setFlag(QGraphicsItem.ItemIsMovable);
        proxy1.setPos(0,30);

        widget2 = QTextEdit();
        proxy2 = self.grScene.addWidget(widget2);
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable);
        proxy2.setPos(0,60);

        line = self.grScene.addLine(-200,-200,400,-100,outllinePen);
        line.setFlag(QGraphicsItem.ItemIsMovable);
        line.setFlag(QGraphicsItem.ItemIsSelectable);


    def loadStylesheet(self, filename):
        print('STYLE loading:', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf-8'))
