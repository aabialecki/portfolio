import finnhub
finnhub_client = finnhub.Client(api_key="sandbox_c251griad3ifpcilkq00")

def quote(stock):
    f_quote = finnhub_client.quote(stock).get("c")
    return f_quote

def search(query):
    if(quote(query) == 0.0):
        return False
    else:
        return True

class Stock:
  #General Info
  ticker = ""
  currPrice = 0 #Price in Cents
  

  #Portfolio Info
  amount = 0
  avgPrice = 0 #Price in Cents
  percent_change = 0.0
  price_change = 0 #Price in Cents

  def __init__(self, ticker, amount, avgPrice):
    self.ticker = ticker
    self.amount = int(amount)
    self.avgPrice = int(avgPrice)
    self.currPrice = quote(ticker)*100 #*100 because price is in cents
    self.percent_change = (self.currPrice-avgPrice)/avgPrice
    self.price_change = self.currPrice*amount - avgPrice*amount

  #Stock Get Methods for Printing
  def get_ticker(self):
      return(self.ticker) 
  def get_amount(self):
      return(self.amount) 
  def get_avgPrice(self):
      return('$'+str(round(self.avgPrice/100,2))) 
  def get_currPrice(self):
      return('$'+str(round(self.currPrice/100, 2))) 
  def get_percent_change(self):
      return(str(round(self.percent_change*100, 1))+'%') 
  def get_price_change(self):
      return('$'+str(round(self.price_change/100,2)))

  #Stock Get Methods for Math
  def num_currPrice(self):
      return(round(self.currPrice/100,2))
  def num_avgPrice(self):
      return(round(self.avgPrice/100,2))


  


  

