import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QStringListModel
import requests
from bs4 import BeautifulSoup

class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.tb = QTextBrowser()
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.tb, 2, 0, 1, 4)

        self.setLayout(grid)

        self.setWindowTitle('크롤러')
        self.setGeometry(100, 100 , 550 ,650)
        self.show()


        url = 'https://cse.pusan.ac.kr'
        r = requests.get(url+'/cse/index.do')
        html = r.content
        soup = BeautifulSoup(html, 'html.parser')
        titles_html = soup.select('#recentBbsArtclObj_757_1281 > li > a > strong')
        day_html = soup.select('#recentBbsArtclObj_757_1281 > li > a > span')
        link_html = soup.select('#recentBbsArtclObj_757_1281 > li > a')

        titles_html2 = soup.select('#recentBbsArtclObj_756_1280 > li > a > strong')
        day_html2 = soup.select('#recentBbsArtclObj_756_1280 > li > a > span')
        link_html2 = soup.select('#recentBbsArtclObj_756_1280 > li > a')

        self.tb.append('학부 공지사항\n')

        for i in range(len(titles_html)):
            titles = titles_html[i].text.split('\n')
            day = day_html[i].text
            link = url + link_html[i].get('href')
            self.tb.append(day + '. ' + titles[0] + ' (' + '<a href="' + link + '">링크</a>' + ')')

        self.tb.append('\n채용게시판\n')
        for i in range(len(titles_html2)):
            titles = titles_html2[i].text.split('\n')
            day = day_html2[i].text
            link = url + link_html2[i].get('href')
            self.tb.append(day + '. ' + titles[0] + ' (' + '<a href="' + link + '">링크</a>' + ')')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec())