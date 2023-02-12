from dotenv import load_dotenv
import os
import random
from API import YeOldeCredit_API

#load the environment variables from the .env file - method to do so found on Twilio "Working with Environment Variables in Python" (https://www.twilio.com/blog/environment-variables-python)
load_dotenv()
JWT=os.getenv("JWT")

#Construct the API class
api = YeOldeCredit_API(JWT)

#Phase 1 - Identifying the account with a bad credit score
def phase1_setup():
    goodCreditScoreAccount_1 = api.getAccountData("creditScore", "gte:580")
    if goodCreditScoreAccount_1["status"] != 200:
        goodCreditScoreAccount_1 = api.getAccountData("creditScore", "gte:580")
    goodCreditScoreAccount_2 = api.getAccountData("creditScore", "gte:580")
    if goodCreditScoreAccount_2["status"] != 200:
        goodCreditScoreAccount_1 = api.getAccountData("creditScore", "gte:580")
    badCreditScoreAccount = api.getAccountData("creditScore", "lt:580")
    if badCreditScoreAccount["status"] != 200:
        badCreditScoreAccount = api.getAccountData("creditScore", "lt:580")

    goodCreditScoreAccount_1_account = goodCreditScoreAccount_1["account"]
    goodCreditScoreAccount_2_account = goodCreditScoreAccount_2["account"]
    badCreditScoreAccount_account = badCreditScoreAccount["account"]

    goodCreditScoreAccount_1 = "Balance: " + goodCreditScoreAccount_1_account["balance"] + " " + goodCreditScoreAccount_1_account["currencyCode"] + "\nCredit Score: "+ goodCreditScoreAccount_1_account["creditScore"]+"\nRisk Score: "+ goodCreditScoreAccount_1_account["riskScore"]
    goodCreditScoreAccount_2 = "Balance: " + goodCreditScoreAccount_2_account["balance"] + " " + goodCreditScoreAccount_2_account["currencyCode"] + "\nCredit Score: "+ goodCreditScoreAccount_2_account["creditScore"]+"\nRisk Score: "+ goodCreditScoreAccount_2_account["riskScore"]
    badCreditScoreAccount = "Balance: " + badCreditScoreAccount_account["balance"] + " " + badCreditScoreAccount_account["currencyCode"] + "\nCredit Score: "+ badCreditScoreAccount_account["creditScore"]+"\nRisk Score: "+ badCreditScoreAccount_account["riskScore"]
    return [{"accountCreditScore": "good", "account": goodCreditScoreAccount_1}, {"accountCreditScore": "good", "account": goodCreditScoreAccount_2}, {"accountCreditScore": "bad", "account": badCreditScoreAccount}]

#Phase 2 - Does the account have any fraudulant transactions?
def phase2_setup():
    api.setAccountIDs()
    accountIDs = api.getAccountIDs()
    transactionList = []
    while transactionList == []:
        randomAccountID = random.choice(accountIDs)
        returnedAccount = api.getAccountByID(randomAccountID)["account"]["Accounts"][0]
        returnedTransactions = api.getTransactionIDs(randomAccountID)["transactions"]
        if len(returnedTransactions) > 2:
            returnedTransactions = returnedTransactions[:2]
        for transactionID in returnedTransactions:
            transaction = api.getTransactionByID(randomAccountID, transactionID)["transaction"]
            transaction_relevantData = "Amount: "+str(transaction["amount"])+"\nMerchant: "+ transaction["merchant"]["name"]+"Message: " + transaction["message"]
            transactionList.append(transaction_relevantData)
    fraudulentTransaction = api.createFraudulentTransactions(randomAccountID)
    fraud_object = fraudulentTransaction["transaction"][0]
    fraudulentTransaction_relevantData = "Amount: "+str(fraud_object["amount"])+"\nMerchant: "+ fraud_object["merchant"]["name"]+"\nMessage: " + fraud_object["message"]
    transactionList.append(fraudulentTransaction_relevantData)
    account_relevantData = {"firstName": returnedAccount["firstname"], "lastName": returnedAccount["lastname"]}

    returningObject = {"account": account_relevantData, "transactions": transactionList}
    print(returningObject)
    return returningObject