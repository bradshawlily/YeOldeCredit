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

    #Returns two accounts who possess good credit scores 
    def getGoodCreditAccounts(self):
        #The FICO Credit Scores Ranges will be used in this application - information about these ranges was found on Capital One "What Is a Credit Score Range?" (https://www.capitalone.com/learn-grow/money-management/credit-score-ranges/)
        #A 'Good' Credit Score is more than or equal to 580 ('Fair' or better), according to the FICO Credit Scores Ranges
        params = {
            'creditScore': 'gte:580',
        }

        response = requests.get("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts", headers=self.headers, params=params)
        response_statusCode = response.status_code
        response_JSON = response.json()["Accounts"]
        account_1 = response_JSON[0]
        account_2 = response_JSON[1]
        account_1_object = {"balance":account_1["balance"], "creditScore": account_1["creditScore"], "currencyCode":account_1["currencyCode"], "riskScore":account_1["riskScore"], "state": account_1["state"]}
        account_2_object = {"balance":account_2["balance"], "creditScore": account_2["creditScore"], "currencyCode":account_2["currencyCode"], "riskScore":account_2["riskScore"], "state": account_2["state"]}

        returningObject = {"status": response_statusCode, "account_1": account_1_object, "account_2": account_2_object}
        return returningObject


    #Returns an account that possesses a bad credit score
    def getBadCreditAccounts(self):
        #A 'Bad' Credit Score is less than 580 (less than 'Fair'), according to the FICO Credit Scores Ranges
        params = {
            'creditScore': 'lt:580',
        }

        response = requests.get("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts", headers=self.headers, params=params)
        response_statusCode = response.status_code #The status code will be included in the returning object to ensure a 200 was returned, handling the error if not
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
print(api.getBadCreditAccounts())