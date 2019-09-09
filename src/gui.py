import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap, QIcon

from imgurDL import Ui_Dialog

from classes.tabs.tabaccountaction import SubmitButton
from classes.tabs.tabdownloadaction import DownloadButton
from classes.tabs.tabactivitylog import ActivityTab


class ImgurDL_AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # icon logo
        self.setWindowIcon(QIcon("media/imgur_icon.png"))

        # initialize classes
        submitbutton = SubmitButton()
        dlbutton = DownloadButton()
        activitytab = ActivityTab()

        # static window
        self.setFixedSize(self.size())

        # icon
        self.ui.label_icon.setPixmap(QPixmap("media/imgur_icon.png"))

        # for tab with yaml
        self.ui.clientIDLineEdit.setMaxLength(40)
        self.ui.clientSecretLineEdit.setMaxLength(40)
        clientid, clientsecret = submitbutton.showCreds()
        self.ui.clientIDLineEdit.setText(clientid)
        self.ui.clientSecretLineEdit.setText(clientsecret)
        self.ui.pushButton_submit.clicked.connect(
            lambda: submitbutton.CollectCreds(
                self.ui.clientIDLineEdit.text(),
                self.ui.clientSecretLineEdit.text()
            )
        )

        # for the help (?) link
        self.ui.label_help.setOpenExternalLinks(True)
        self.ui.label_help.setText('<a href="https://api.imgur.com/oauth2/addclient">?</a>')

        # for tab with url
        self.ui.postURLLineEdit.setMaxLength(200)
        self.ui.downloadToLineEdit.setMaxLength(40)
        self.ui.pushButton_download.clicked.connect(
            lambda: dlbutton.downloadLabels(self.ui.postURLLineEdit.text(), self.ui.downloadToLineEdit.text()))
        self.ui.pushButton_download.clicked.connect(lambda: dlbutton.warnUser(self))

        # for downnload path
        filePath = dlbutton.defaultDir()
        self.ui.downloadToLineEdit.setText(filePath)
        self.ui.pushButton_fileExplorer.clicked.connect(lambda: dlbutton.browseFiles(self))

        # update values live
        self.ui.label_credits.setText(dlbutton.creditsLeftOutput)

        # activity tab
        activitytab.log2Table(self.ui.tableWidget_activity)
        self.show()

app = QApplication(sys.argv)
appWin = ImgurDL_AppWindow()
appWin.show()
sys.exit(app.exec_())
