import yaml

from ..log.loggingpost import LoggingErrors
from ..read.readconfigs import ReadYaml

#put these into a method
from ..calls.initializeimgur import InitializeImgurAPIs
from ..calls.postDownloader import downloadEntirePost
#0cd9faea686acec 84cd3fcc0dcd04d6559f1b9640cef2dc70621fb
#from # HOW DO I PULL FROM GUI
from .tabdownloadaction import DownloadButton

class SubmitButton():
    def CollectCreds(self, clientID, sharedSecret):
        try:
            if (clientID == ""):
                raise ValueError("Client ID is empty")
        except ValueError as val_err:
            LoggingErrors("error.log", str(val_err))
        try:
            if (sharedSecret == ""):
                raise ValueError("Client Secret is empty")
        except ValueError as val_err:
            LoggingErrors("Error.log", str(val_err))
        # else:
        #	print("not empty")
        if (clientID != "" and sharedSecret != ""):
            print("write to yaml file" + clientID + sharedSecret)
            with open("config/setup.yaml") as yaml_stream:
                configs = yaml.safe_load(yaml_stream)
            configs['credentials']['client_id'] = clientID
            configs['credentials']['client_secret'] = sharedSecret
            with open("config/setup.yaml", 'w') as yaml_stream:
                yaml.dump(configs, yaml_stream)
            del yaml_stream
            connSuccess = InitializeImgurAPIs.initializeImgurCalls()
            creditsLeftOutput = "Connection unsuccessful"
            if (connSuccess == True):
                creditsLeftOutput = downloadEntirePost.creditsLeft(downloadEntirePost.client)
            print("hte value is: " + creditsLeftOutput)
            dlbutton = DownloadButton()
            self.ui.label_credits.setText(dlbutton.creditsLeftOutput)


    def showCreds(self):
        credentials = ReadYaml("credentials").yamldict
        client_id = credentials["client_id"]
        client_secret = credentials["client_secret"]
        return [client_id, client_secret]
