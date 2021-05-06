from pytube import YouTube
from PyQt5.QtWidgets import *
import sys


class youtubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()
    def ui_init(self):
        self.buton1=QPushButton("İndir")
        self.buton2=QPushButton("Temizle")
        self.linkArea=QLineEdit()
        self.setWindowTitle("Youtube Video Downloader")
        self.setFixedSize(400,300)
        self.buton1.clicked.connect(self.indir)
        self.buton2.clicked.connect(self.temizle)
        hBox=QHBoxLayout()
        hBox.addStretch()
        hBox.addWidget(self.linkArea)
        hBox.addStretch()

        hBox1 = QHBoxLayout()
        hBox1.addStretch()
        hBox1.addWidget(self.buton2)
        hBox1.addStretch()

        hBox2 = QHBoxLayout()
        hBox2.addStretch()
        hBox2.addWidget(self.buton1)
        hBox2.addStretch()

        
        vBox=QVBoxLayout()
        vBox.addLayout(hBox)
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)
        self.show()

    def indir(self):
        yt=YouTube(self.linkArea.text())
        videos=yt.streams.filter(progressive=True)
        for video in videos:
            video.download()
    
    def temizle(self):
        self.linkArea.clear()
    





if __name__=="__main__":
    app=QApplication(sys.argv)
    ytd=youtubeDownloader()
    sys.exit(app.exec_())
