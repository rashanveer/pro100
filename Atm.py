class atm :
    def __init__(self,atmcardnumber,pinnumber):
        self.atmcardnumber = atmcardnumber
        self.pinnumber = pinnumber

CashWithDrawl = atm("4545","2087")
print("got my cash!")
BalanceEnquiry = atm("2207","3321")
print("ok,I got the details")