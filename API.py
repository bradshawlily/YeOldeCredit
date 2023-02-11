import json
import requests
import os
from dotenv import load_dotenv

class API:
    def __init__(self, JWT):
        self.JWT = JWT
        self.headers = {
            'Authorization': f'Bearer {JWT}',
            'Content-Type': 'application/json',
            'version': '1.0'
        }

    def createARandomAccount(self):
        quantity = 1
        numTransactions = 5
        liveBalance = False
        payload = json.dumps({"quantity": quantity, "numTransactions": numTransactions, "liveBalance": liveBalance})

        response = requests.post("https://sandbox.capitalone.co.uk/developer-services-platform-pr/api/data/accounts/create", headers=self.headers, data=payload)
        return response.status_code

load_dotenv()
JWT=os.getenv("JWT")
api = API(JWT)
print(api.createARandomAccount())