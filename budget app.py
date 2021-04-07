class Budget:
  def __init__(self, category): 
        self.inventory = []
        self.amount = 0
        # categories can include food, entertainment, etc
        self.category = category
        
  # check if you have enough funds for transactions     
  def check_funds(self, amount):
    if self.amount < amount:
        print('Not enough funds')
        return False
    else:
        print('Funds dey')
        return True

  # Deposit money to specificcategory
  def deposit_amount(self, amount, description=""):
    # The "" in the description parameter will return a blank string if the user does not enter anything
    self.inventory.append({"amount":amount,"description":description})
    self.amount += amount

  # Withdraw money from specific category
  def withdraw_amount(self, amount, description=""):
    if self.check_funds(amount) == True:
      self.amount -= amount
      self.inventory.append({"amount":-amount,"description":description})
      return True
    else:
      return False

  # return balanace of budget 
  def compute_balance(self):
    return self.amount

  def transfer_amount(self, amount, category):
    if self.check_funds(amount) == True:
      self.amount -= amount
      self.inventory.append({"amount": -amount,"description":"Transfer to "+category.category})
      category.inventory.append({"amount": amount,"description": "Transfer from "+self.category})
      return True
    else:
      return False
