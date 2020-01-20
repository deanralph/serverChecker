import json
import os

class ServerControl():

    def __init__(self, serverName):
        self.serverName = serverName

    def createNewCheck(self, serviceName, checkType):
        self.serviceName = serviceName
        self.checkType = checkType
        self.fileName = f"{self.serverName}-{self.serviceName}.json"
        with open(os.path.join("checkconfig", self.fileName), "w") as f:
            json.dump(tempDict,f, indent=2)
        if os.path.exists(os.path.join("checkconfig", self.fileName)):
            return f"Success creating {self.fileName}"
        else:
            return f"Error creating {self.fileName}"

    def loadExsistingCheck(self):
        self.fileName = f"{self.serverName}-{self.serviceName}.json"
        if os.path.exists(os.path.join("checkconfig", self.fileNamee)):
            with open(os.path.join("checkconfig", self.fileName), "r") as f:
                varReturn = json.load(f)
            self.serviceName = varReturn["Service"]
            self.checkType = varReturn["CheckType"]
        else:
            varReturn = "Error - Json file not fount"

        return varReturn
