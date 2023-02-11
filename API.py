import json
import requests
import os
from dotenv import load_dotenv

#The class that communicates with the Capital One API service
class API:
    def __init__(self, JWT):
        self.JWT = JWT
        self.headers = {
            'Authorization': f'Bearer {JWT}',
            'Content-Type': 'application/json',
            'version': '1.0'
        }

    #Creates a random account for use in application, returning a status code
    def createARandomAccount(self):
        quantity = 1
        numTransactions = 5
        liveBalance = False
        payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})

        response = requests.post("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create", headers=self.headers, data=payload)
        return response.status_code

    #Returns relevant data from an account based on the parameter
    #This function was refactored from two functions, one returning data from an account that had a 'Good' credit score and another returning data from an account that had a 'Bad' credit score 
    def getAccountData(self, parameter):
        #The FICO Credit Scores Ranges will be used in this application - information about these ranges was found on Capital One "What Is a Credit Score Range?" (https://www.capitalone.com/learn-grow/money-management/credit-score-ranges/)
        #A 'Good' Credit Score is more than or equal to 580 ('Fair' or better), according to the FICO Credit Scores Ranges
        #A 'Bad' Credit Score is less than 580 (less than 'Fair'), according to the FICO Credit Scores Ranges
        params = {
            "creditScore": parameter
        }

        response = requests.get("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts", headers=self.headers, params=params)
        response_statusCode = response.status_code
        response_JSON = response.json()["Accounts"]
        account = response_JSON[0]
        account_object = {"balance":account["balance"], "creditScore": account["creditScore"], "currencyCode":account["currencyCode"], "riskScore":account["riskScore"], "state": account["state"]}
        returningObject = {"status": response_statusCode, "account": account_object}
        return returningObject

#load the environment variables from the .env file - method to do so found on Twilio "Working with Environment Variables in Python" (https://www.twilio.com/blog/environment-variables-python)
load_dotenv()
JWT=os.getenv("JWT")

#Testing section
api = API(JWT)
print("Good:")
print(api.getAccountData("gte:580"))
print("Bad:")
print(api.getAccountData("lt:580"))