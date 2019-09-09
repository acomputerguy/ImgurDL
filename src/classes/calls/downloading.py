import os, zipfile

from hurry.filesize import size
from urllib.request import urlretrieve

from ..log.loggingpost import LoggingErrors

class Downloading():
    def __init__(self, postInfo, filePath):
        self.postInfo = postInfo
        self.filePath = filePath

    def action(self):
        for key, val in self.postInfo.items():
            self.makeDir(key)
            self.generateLogs(key, val[0], val[1], val[2])
            self.downloadImages(val[3])
            self.wrapUp()

    def makeDir(self, dirName):
        self.dirName = dirName
        dirName = self.filePath + dirName
        dirNameZip = dirName + ".zip"

        self.zipped = zipfile.ZipFile(dirNameZip, 'w', compression=zipfile.ZIP_LZMA)

        if not os.path.exists(dirName):
            os.makedirs(dirName)
        return

    def generateLogs(self, title, numImages, postLink, postSize):
        LoggingErrors("activity.log", title + "|" + postLink + "|" + str(numImages) + "|" + str(size(postSize)))
        return

    def downloadImages(self, imageDict):
        for imageURL, filePathDL in imageDict.items():
            fullFilePathDL = self.filePath + filePathDL
            urlretrieve(imageURL, fullFilePathDL)
            self.zipped.write(fullFilePathDL, filePathDL, compress_type=zipfile.ZIP_DEFLATED)
            os.remove(fullFilePathDL)

    def wrapUp(self):
        self.zipped.close()
        deleteDir = self.filePath + self.dirName
        os.removedirs(deleteDir)