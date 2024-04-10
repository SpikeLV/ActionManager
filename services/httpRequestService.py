import requests, json
from requests.adapters import HTTPAdapter

import urllib3
from urllib3.util import Retry
import logging


class httpRequestService:
    def __init__(self):
        self.lost = 0
        self.responseJson = []

        logging.basicConfig(
            filename='log/httpRequestService.log',  # Specify the file name
            level=logging.DEBUG,      # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

        #self.requestSession = requests.Session()
        
        retry_strategy = Retry(total=3, backoff_factor=0.3)
        self.http = urllib3.PoolManager(retries=retry_strategy)

    def sendRequest(self, url:str):
        try:
            if self.lost != 1:
                #print("aaaa ", url)
                rep = self.http.request("GET", url, timeout=3)                
                return True

        except urllib3.exceptions.TimeoutError:
            print("Request timed out.")
            return None
        except urllib3.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}") 
            return None
        except Exception as e:
            print("Error! Waiting secs and re-trying...")
            print(e)
            return None
        
    def getStatus(self, url:str):
        try:
            if self.lost != 1:
                #print(url)
                rep = self.http.request("GET", url, timeout=3)
                #print(rep.json())       
                return self.handleResponse(reply=rep)

        except urllib3.exceptions.TimeoutError:
            print("Request timed out.")
            return None
        except urllib3.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}") 
            return None
        except Exception as e:
            print("Error! Waiting secs and re-trying...")
            print(e)
            return None
        
    def handleResponse(self, reply:object):
        try:
            return reply.json()
        except Exception as e:
            print("JSON Error! ")
            print(e)