from imgurpython.helpers.error import ImgurClientError

from ..log.loggingpost import LoggingErrors
from .creditsandcountdown import *
from .downloading import *

import signal, sys

class downloadEntirePost():
    totaldlsize = 0
    postInfo = {}
    client = ""
    fileNm = ""

    def signal_handle(signal, handle):
        print(' Exiting application...')
        sys.exit(0)

    def albumParse(client, albumList, postInfo):
        totalDownloadSize = 0
        postDownloadSize = 0
        urlAndfilePath = {}
        if len(albumList) < 2:
            albumInfo = client.get_album(albumList[0])
            images = client.get_album_images(albumList[0])

            postDownloadSize, urlAndfilePath = downloadEntirePost.imageParser(images, albumInfo.title, urlAndfilePath)
            postInfo[albumInfo.title] = [albumInfo.images_count, albumInfo.link, postDownloadSize, urlAndfilePath]

            totalDownloadSize += postDownloadSize
        else:
            for album in albumList:
                albumInfo = client.get_album(album)
                images = client.get_album_images(album)

                postDownloadSize, urlAndfilePath = downloadEntirePost.imageParser(images, albumInfo.title,
                                                                                  urlAndfilePath)
                postInfo[albumInfo.title] = [albumInfo.images_count, albumInfo.link, postDownloadSize, urlAndfilePath]

                totalDownloadSize += postDownloadSize
        return totalDownloadSize, postInfo

    def imageParser(images, title, urlAndfilePath):
        imageSize = 0
        urlAndfilePath = {}
        for image in images:
            extn = image.type.split('/')
            fileNm = image.id + "." + extn[1]
            filePath = title + "/" + fileNm
            print(fileNm)
            urlAndfilePath.update({image.link: filePath})

            imageSize = image.size + imageSize
        return imageSize, urlAndfilePath

    def creditsLeft(client):
        credits = client.get_credits()
        CreditsCount = Leftovers(credits)
        creditsNowIs = CreditsCount.calculateCredits()
        return creditsNowIs

    def checkIfUrlIsValid(client, albumList):
        print("checking")
        for album in albumList:
            try:
                client.get_album(album)
            except ImgurClientError as imgur_err:
                LoggingErrors("error.log", str(imgur_err.status_code) + "---" + str(imgur_err.error_message))
                albumList.remove(album)
        return albumList

    def urlInfo(urlLine):

        countChar = 0
        albumList = []
        for chara in urlLine:
            if chara == ' ':
                countChar = countChar + 1
        if countChar == 0:
            albumList = [urlLine[urlLine.rfind('/') + 1:]]
        else:
            arrURLs = urlLine.split(" ")
            for url in arrURLs:
                if (url == ""):
                    continue
                albumList.append((url[url.rfind('/') + 1:]))
        albumList = downloadEntirePost.checkIfUrlIsValid(downloadEntirePost.client, albumList)

        if albumList:
            postInfo1 = {}
            totalDownloadSize, postInfo1 = downloadEntirePost.albumParse(downloadEntirePost.client, albumList,
                                                                         postInfo1)
            downloadEntirePost.totaldlsize = totalDownloadSize
            downloadEntirePost.postInfo = postInfo1
            print("totaldlsize: " + str(downloadEntirePost.totaldlsize))
            print("postinfo: " + str(postInfo1))

    def downloadAction(filePath):
        downloading = Downloading(downloadEntirePost.postInfo, filePath)
        downloading.action()