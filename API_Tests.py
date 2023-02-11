import unittest
import os
from dotenv import load_dotenv
from API import YeOldeCredit_API

load_dotenv()
JWT=os.getenv("JWT")
api = YeOldeCredit_API(JWT)

class Test_API(unittest.TestCase):

    ##Testing the createARandomAccount function
    def test_createARandomAccount(self):
        self.assertEqual(api.createARandomAccount(), 200, "The returning status code should be 200")

    ##Testing the getAccountIDs function

    ##Testing the setAccountIDs function

    ##Testing the getTransactionIDs function

    ##Testing the createFraudulentTransactions function

    ##Testing the getAccountByID function

    ##Testing the getTransactionByID function

    ##Testing the getAccountData function


#Main testing function
def main():
    unittest.main()

main()