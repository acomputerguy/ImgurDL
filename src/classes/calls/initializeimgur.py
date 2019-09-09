from imgurpython import ImgurClient
from ..log.loggingpost import LoggingErrors
from ..read.readconfigs import ReadYaml
from imgurpython.helpers.error import ImgurClientError
from ..calls.postDownloader import downloadEntirePost

class InitializeImgurAPIs():
    def yamlInfo():
        credentials = ReadYaml("credentials").yamldict
        client_id = credentials["client_id"]
        client_secret = credentials["client_secret"]
        return [client_id, client_secret]

    def initializeImgurCalls():
        idcred, secret = InitializeImgurAPIs.yamlInfo()
        try:
            downloadEntirePost.client = ImgurClient(idcred, secret)
            return True
        except ImgurClientError as imgur_err:
            LoggingErrors("error.log", str(imgur_err.status_code) + " " + str(imgur_err.error_message))
            return False
