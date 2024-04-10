
from services.config import config
from services.httpRequestService import httpRequestService

class LogicService:
    def __init__(self):
        self.lost = 0
        self.requestUrl = []
        self.mains = []
        
        for main_url in config["logic-status"]:
            self.mains.append(main_url)

        self.logicRequest = httpRequest()

    def addUrl(self, url:str):
        if self.lost != 1:
            self.requestUrl.append(url)
        
    def getStatus(self):
        if self.lost != 1:
            if len(self.requestUrl) !=0:
                index = 0
                while index < len(self.requestUrl):
                    urlFromList = self.requestUrl.pop(0)
                    resultJson = self.logicRequest.sendRequest(url=urlFromList)      #device activation call

            else:
                for main in self.mains:
                    resultJson = self.logicRequest.getStatus(url=main['url'])      #MAIN status check
                    if resultJson:
                        if resultJson['status'] != "ok":
                            self.lost = 1
                            print("Main status:error")
                            return
                        else:
                            self.lost = 0
                            self.handleResponse(responseJson=resultJson)
                    else:
                        self.requestUrl = []
                        self.lost = 1
            if self.checkTh:
                for thUrl in self.th:
                    resultJson = self.logicRequest.getStatus(url=thUrl)      #TH call
                    if resultJson:
                        self.handleResponse(responseJson=resultJson)
                self.checkTh = False
                
    def handleResponse(self, responseJson:dict):
        self.logicTimer += 1

        if "GS" in responseJson.keys():
            self.devices["GS"].update(responseJson["GS"])
        if "PT" in responseJson.keys():
            self.devices["PT"].update(responseJson["PT"])

        if "TH_D" in responseJson.keys():
            self.devices['TH'].append(responseJson["TH_D"])


    def sendRequest(self, deviceName:str, event:str):
        for main in self.mains:
            for item in main["GS"]:
                if item == deviceName:
                    url = main["url"]+"/"+deviceName+"/"+event
                    self.addUrl(url=url)
                    break
            for item in main["PT"]:
                if item == deviceName:
                    url = main["url"]+"/"+deviceName+"/"+event
                    self.addUrl(url=url)
                    break
            for item in main["other"]:
                if item == deviceName:
                    url = main["url"]+"/"+deviceName+"/"+event
                    self.addUrl(url=url)
                    break

        #print(url+"/"+deviceName+"/"+event)