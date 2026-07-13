class bankaccount:
   def __init__(self,initial_Balance=500):
      self.balance=initial_Balance
      

   def withdraw(self,amount):
      
      if amount<=0:
         print("The amount must be greater than 0.")
         return
      if amount>self.balance:
         print("Insufficient amount in your account.")
         return
         
      
      current_amount = self.balance-amount
      print(f"Initial Balance:{self.balance}")
      print(f"Withdrawn:{amount}")
      print(f"Current Balance:{current_amount}")

   def deposit(self,amount):
      if amount<=0:
         print("The amount must be greater than 0.")
         return
      
      current_amount = self.balance+amount
      print(f"Initial Balance:{self.balance}")
      print(f"Deposite:{amount}")
      print(f"Current Balance:{current_amount}")
         

b1=bankaccount()
b1.withdraw(400)
b1.deposit(200)

      

      
   
   
   