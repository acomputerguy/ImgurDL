from PyQt5.QtWidgets import QMessageBox, QFileDialog

from os.path import expanduser
from hurry.filesize import size
import yaml

from ..log.loggingpost import LoggingErrors
from ..read.readconfigs import ReadYaml
from ..calls.postDownloader import downloadEntirePost
from ..calls.initializeimgur import InitializeImgurAPIs

class DownloadButton():
    connSuccess = InitializeImgurAPIs.initializeImgurCalls()
    creditsLeftOutput = "Connection unsuccessful"
    if(connSuccess == True):
        creditsLeftOutput = downloadEntirePost.creditsLeft(downloadEntirePost.client)

    def defaultDir(self):
        filePathAsConfig = ReadYaml("configuration").yamldict
        downloadDir = filePathAsConfig["file_path"]
        return downloadDir

    def downloadLabels(self, url, dlPath):
        print("download images")
        try:
            if (url == ""):
                raise ValueError("Imgur URL line is empty")
        except ValueError as val_err:
            LoggingErrors("error.log", str(val_err))
        try:
            if (dlPath == ""):
                raise ValueError("Download file path is empty")
        except ValueError as val_err:
            LoggingErrors("error.log", str(val_err))

    def warnUser(self, object):
        downloadEntirePost.urlInfo(object.ui.postURLLineEdit.text())
        dlSize = size(downloadEntirePost.totaldlsize)
        buttonReply = QMessageBox.warning(object, 'Warning', "You are about to download " + dlSize + ". Proceed?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            filePath = object.ui.downloadToLineEdit.text() + "/"
            downloadEntirePost.downloadAction(filePath)
        # progress bar
        else:
            print('No clicked.')

    def browseFiles(self, object):
        downloadDir = str(expanduser("~"))
        downloadDir = QFileDialog.getExistingDirectory(object, "Download to", downloadDir, QFileDialog.ShowDirsOnly)
        object.ui.downloadToLineEdit.setText(downloadDir)
        filePath = {'configuration': {'file_path': downloadDir }}
        yaml_streamw = open("setup.yaml", 'w')
        yaml.dump(filePath, yaml_streamw, default_flow_style=False)
        del yaml_streamw
