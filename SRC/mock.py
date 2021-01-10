
class User:
    def __init__(self,name,age,accounts):
        self.name=name
        self.age=age
        self.accounts=accounts

    def return_available_funds(self):
        available_funds = 0
        for account in self.accounts:
            available_funds += account.get_balance()  #klass account i metoda get_balance -nie many musimy zrobić mocki
        return available_funds