import sys
import copy
import random
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QToolTip, QSystemTrayIcon, QMenu, QAction, QInputDialog, QMessageBox, QApplication, qApp
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon, QFont

def wordnum():
    with open("word.txt", "r") as f:
        data = f.read()
        word = data.split('\n')
        num = len(word)
    return num, word

class Myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.idx = 0
        self.num, self.word = wordnum()
        start = self.word[0].split()
        self.qle = QLabel(start[0], self)
        self.qle.setAlignment(Qt.AlignCenter)
        self.qle2 = QLabel(start[1], self)
        self.qle2.setAlignment(Qt.AlignCenter)
        self.qle3 = QLabel(str(self.idx+1), self)
        self.qle3.setAlignment(Qt.AlignCenter)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):

       font1 = self.qle.font()
       font1.setPointSize(10)
       font1.setBold(True)
       font2 = self.qle2.font()
       font2.setPointSize(10)
       font2.setBold(True)
       font3 = self.qle3.font()
       font3.setPointSize(10)
       font3.setBold(True)
       self.qle.setFont(font1)
       self.qle2.setFont(font2)
       self.qle3.setFont(font3)

       leftbutton = QPushButton(self)
       leftbutton.setStyleSheet('background:transparent')
       leftbutton.setIcon(QIcon('icon\left.png'))
       leftbutton.setIconSize(QSize(36, 36))
       leftbutton.setEnabled(True)
       rightbutton = QPushButton(self)
       rightbutton.setStyleSheet('background:transparent')
       rightbutton.setIcon(QIcon('icon\\right.png'))
       rightbutton.setIconSize(QSize(36, 36))
       rightbutton.setEnabled(True)

       hbox = QHBoxLayout()
       hbox.addStretch(1)
       hbox.addWidget(leftbutton)
       hbox.addWidget(self.qle3)
       hbox.addWidget(rightbutton)
       hbox.addStretch(1)

       layout = QVBoxLayout()
       layout.addWidget(self.qle)
       layout.addWidget(self.qle2)
       layout.addLayout(hbox)

       self.setLayout(layout)

       leftbutton.clicked.connect(self.leftfunc)
       rightbutton.clicked.connect(self.rightfunc)

       QToolTip.setFont(QFont('Sanserif', 10))

       trayIcon = QSystemTrayIcon(QIcon('icon\\title.png'), self)
       trayIcon.setToolTip('단어 암기 프로그램')
       menu = QMenu()
       exitAction = QAction('Exit', self)
       exitAction.triggered.connect(qApp.quit)
       menu.addAction(exitAction)

       testmenu = menu.addMenu('단어 테스트')
       hangulAction = QAction('뜻 테스트', self)
       hangulAction.triggered.connect(self.hangultestfunc)
       englishAction = QAction('영어 테스트', self)
       englishAction.triggered.connect(self.Englishtestfunc)
       testmenu.addAction(hangulAction)
       testmenu.addAction(englishAction)

       menu.addSeparator()
       menu.addAction(exitAction)
       trayIcon.setContextMenu(menu)
       trayIcon.show()

       self.setWindowTitle("Word")
       #self.setStyleSheet("background-color: #87CEFA;")
       self.setWindowIcon(QIcon('icon\\title.png'))
       self.setGeometry(300, 100, 200, 100)
       self.show()

    #한글테스트 클릭시 한글테스트 화면으로 가서 테스트 진행
    def hangultestfunc(self):
        wordcp = copy.deepcopy(self.word)
        random.shuffle(wordcp)
        for i in wordcp:
            wo = i.split()
            text, ok = QInputDialog.getText(self, '뜻 퀴즈', wo[0])
            if ok:
                msgBox = QMessageBox()
                msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
                if wo[1] == text:
                    msgBox.setWindowTitle('정답')
                    msgBox.setText(wo[1])
                else:
                    msgBox.setWindowTitle('오답')
                    msgBox.setText(wo[1])

                msgBox.move(self.pos().x(), self.pos().y())
                msgBox.setStyleSheet("QLabel{min-width: 150px;}")
                msgBox.exec()
            else:
                break

    def Englishtestfunc(self):
        wordcp = copy.deepcopy(self.word)
        random.shuffle(wordcp)
        for i in wordcp:
            wo = i.split()
            text, ok = QInputDialog.getText(self, '영어 퀴즈', wo[1])
            if ok:
                msgBox = QMessageBox()
                msgBox.setWindowFlags(Qt.WindowStaysOnTopHint)
                if wo[0] == text:
                    msgBox.setWindowTitle('정답')
                    msgBox.setText(wo[0])
                else:
                    msgBox.setWindowTitle('오답')
                    msgBox.setText(wo[0])
                msgBox.move(self.pos().x(), self.pos().y())
                msgBox.setStyleSheet("QLabel{min-width: 150px;}")
                msgBox.exec()
            else:
                break

    def leftfunc(self):
        if self.idx > 0:
            self.idx -= 1
            wo = self.word[self.idx].split()
            self.qle.setText(wo[0])
            self.qle2.setText(wo[1])
            self.qle3.setText(str(self.idx+1))

    def rightfunc(self):
        if self.idx < self.num-1:
            self.idx += 1
            wo = self.word[self.idx].split()
            self.qle.setText(wo[0])
            self.qle2.setText(wo[1])
            self.qle3.setText(str(self.idx+1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec())

