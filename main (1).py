class BankAccount

def__int__(self,account_number,account_holder_name,inital_balance=0.0):
  self.__account_number=accout_number
  self.__account_holder_name=account_holder_name
  self.__account_balance=initial_balance  

def depposit(self,amount):
  if amount>0:
    self.__account_balance + = amount
    print("Deposited ₹{}. New balance ₹{}".format(amount self.__account_balance))
  else:
         print("Invalid deposit amount.please deposit a positive amount")

  def Withdeaw (self, amount):
    if amount>0 and amount<=self.__amount_balance:
      self.__aamount_balance_=amount
      print("Withdeaw ₹{}New balance ₹{}".format(a")