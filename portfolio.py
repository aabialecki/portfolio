from prettytable import PrettyTable
from stock import Stock, search

class Portfolio:
  stocks = [] #Array of Stock Objects

  #Portfolio Statistics
  portfolioValue = 0 #Total Value of Portfolio
  investmentValue = 0#Value of Original Investment
  roi = 0 #Return on investment (%)

  #Updates portfolio statistics 
  def update_stats(self):
    for i in range(len(self.stocks)):
        self.portfolioValue+=self.stocks[i].num_currPrice()*self.stocks[i].get_amount()
        self.investmentValue+=self.stocks[i].num_avgPrice()*self.stocks[i].get_amount()
    self.roi = (self.portfolioValue-self.investmentValue)/self.investmentValue

  def __init__(self, stocklist):
    self.stocks = stocklist
    self.update_stats()
    

  def add_stock(self, query, amount, avgPrice):
    #Check if ticker exists
    if(search(query) == True):
        newStock = Stock(query, int(amount), int(round(float(avgPrice)*100,0))) #*100 is because price is stored in pennies
        isFound = False
        index = 0

        #Checks if stock is already in portfolio
        for i in range(len(self.stocks)):
            if(query == self.stocks[i].ticker):
                index = i
                isFound = True
        #If found, updates avgPrice and amount
        if(isFound == True):
            self.stocks[index].avgPrice = ((int(amount)*int(avgPrice)) + (self.stocks[index].amount*self.stocks[index].avgPrice))/(int(amount)+self.stocks[index].amount)
            self.stocks[index].amount+=int(amount)
        #if not found, adds new stock
        else:
            self.stocks.append(newStock)
        self.update_stats()
    else:
        print(query + " Not Found")

  def remove_stock(self,query):
    #Checks if stock is in portfolio
    for i in range(len(self.stocks)):
        if(query == self.stocks[i].ticker):
            index = i
            isFound = True
    if(isFound==True):
        self.stocks.pop(index)
        self.update_stats()
    else:
        print(query + " not found in portfolio")
  

  #Prints with Default Order (File Order)
  def print_portfolio(self):
    Ptable = PrettyTable()
    Ptable.field_names = ["Ticker","Price", "% Change", "Change", "Amount", "Avg Price"]
    for i in range(len(self.stocks)):
        Ptable.add_row([self.stocks[i].get_ticker(), 
                        self.stocks[i].get_currPrice(), 
                        self.stocks[i].get_percent_change(), 
                        self.stocks[i].get_price_change(),
                        self.stocks[i].get_amount(), 
                        self.stocks[i].get_avgPrice()])
    Ptable.add_row(["Total: ",
                    "$"+str(round(self.portfolioValue,2)),
                    str(round(self.roi*100,1))+"%",
                    "$"+str(round(self.portfolioValue-self.investmentValue,2)),
                    "-----",
                    "-----"])
    Ptable.align = "l"
    print(Ptable)

    