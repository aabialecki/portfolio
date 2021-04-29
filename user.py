from os import listdir
from os.path import isfile, join, splitext
from stock import Stock
from portfolio import Portfolio
userPath = "./users/" 

class User:
    userPortfolio = 0
    username = ""
    logged_in = False

    def __init__(self, username):
        self.username = username
    def set_portfolio(self,portfolio):
        self.userPortfolio=portfolio
    def get_portfolio(self):
        return self.userPortfolio

#returns list of users
def get_user_list():
  userlist = [splitext(f)[0] for f in listdir(userPath) if isfile(join(userPath, f))]
  return userlist

#Read User Portfolio
#Get Stock Price
#Create Portfolio
def login(username):
    stocks = list() #Array of User's Stocks
    user = User(username)

    userFile = open(userPath + username + ".txt")

    count = 0 #Checks how many stocks were added
    for i in userFile:
        line = i.split(",")
        stocks.append(Stock(line[0], #Ticker
                        int(line[1]), #Number of Shares
                        int(line[2]))) #AvgCost (in cents)
        count+=1
    if(count==0):
        print("Empty Portfolio, Addding Default Stock (You may remove this at any time).")
        stocks.append(Stock("AAPL",10,10000))
    user.set_portfolio(Portfolio(stocks))
    user.logged_in = True
    return user

def register(username):
    try:
        userFile = open(userPath + username + ".txt", "w")
    except Exception as e:
        print("Registration Error: " + e)
        return False
    return True

def logout(user):
     userFile = open(userPath + user.username + ".txt", "w")
     stock_list =user.userPortfolio.stocks
     if len(stock_list) < 1:
        print("Logged Out!")
        return
     for i in stock_list:
        userFile.write(i.ticker + "," + str(i.amount) + "," + str(i.avgPrice) + "\n")





