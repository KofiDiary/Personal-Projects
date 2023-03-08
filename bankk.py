Balance = 600
Limit = 1000
Amount = int (input ("Enter amount to withdraw: "))
if Amount > Balance and Amount < Limit:
    print ("You have insufficient balance to perform this transaction")
    print ("You can only withdraw",  Balance)
elif Amount > Balance and Amount > Limit:
    print ("You can't withdraw this amount because your daily transaction is GHS1000.00")
else:
    print ("You can withdraw this amount")
