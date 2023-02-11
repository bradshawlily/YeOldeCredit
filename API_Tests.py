import unittest
import os
from dotenv import load_dotenv
from API import YeOldeCredit_API

load_dotenv()
JWT=os.getenv("JWT")
api = YeOldeCredit_API(JWT)

class Test_API(unittest.TestCase):

    ##Cleaner function ran after every test relating to the accountID attribute to ensure that each test can operate in isolation
    def emptyAccountIDs(self):
        api.accountIDs = []

    ##Testing the createARandomAccount function
    def test_createARandomAccount(self):
        self.assertEqual(api.createARandomAccount(), 200, "The returning status code should be 200")

    ##Testing the getAccountIDs function
    def test_getAccountsIDs_emptyList(self):
        self.assertEqual(api.getAccountIDs(), [], "The accountsIDs attribute should be empty as it has not been set")
        self.emptyAccountIDs()

    def test_getAccountsIDs_populatedList(self):
        api.setAccountIDs()
        self.assertNotEqual(api.getAccountIDs(), [], "The accountsIDs attribute should not be empty as the setAccountsIDs method had been called")
        self.emptyAccountIDs()

    ##Testing the setAccountIDs function
    def test_setAccountIDs(self):
        api.getAccountIDs()
        self.assertEqual(api.getAccountIDs(), [], "The accountsIDs attribute should be empty as it has not been set")
        api.setAccountIDs()
        self.assertNotEqual(api.getAccountIDs(), [], "The accountsIDs attribute should not be empty as the setAccountsIDs method had been called")
        self.emptyAccountIDs()
    
    ##Testing the getTransactionIDs function
    def test_getTransactionIDs(self):
        testAccountID = "78798428"
        expectedTransactionsReturned_length = 23 
        transactionIDs = api.getTransactionIDs(testAccountID)["transactions"]
        self.assertEqual(len(transactionIDs), 23, f"There should be {expectedTransactionsReturned_length} transactions under account {testAccountID}")

    ##Testing the createFraudulentTransactions function
    def test_createFraudulentTransactions(self):
        testAccountID = "53439508"
        fraudulentTransaction_return = api.createFraudulentTransactions(testAccountID)
        return_statusCode = fraudulentTransaction_return["status"]
        return_fraudType = fraudulentTransaction_return["fraudType"]
        return_transaction = fraudulentTransaction_return["transaction"]
        self.assertEqual(return_statusCode, 200, "The returned status code should be 200")
        self.assertNotEqual(return_fraudType, "", "A random fraud type should have been returned")
        self.assertNotEqual(return_transaction, [], "The returned list should not be empty")

    ##Testing the getAccountByID function
    def test_getAccountByID(self):
        testAccountID = "15085119"
        getAccountByID_return = api.getAccountByID(testAccountID)
        return_statusCode = getAccountByID_return["status"]
        return_transaction = getAccountByID_return["transaction"]
        self.assertEqual(return_statusCode, 200, "The returned status code should be 200")
        self.assertNotEqual(return_transaction, [], "The returned list should not be empty")

    ##Testing the getTransactionByID function
    def test_getTransactionByID(self):
        testAccountID = "78798428"
        testTransactionID = "fc6bef1c-470e-47b3-aa84-03126c4f49f9"
        getTransactionByID_return = api.getTransactionByID(testAccountID, testTransactionID)
        return_statusCode = getTransactionByID_return["status"]
        return_transaction = getTransactionByID_return["transaction"]
        self.assertEqual(return_statusCode, 200, "The returned status code should be 200")
        self.assertNotEqual(return_transaction, [], "The returned list should not be empty")

    ##Testing the getAccountData function


#Main testing function
def main():
    unittest.main()

main()