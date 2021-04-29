import user
from portfolio import Portfolio
from prettytable import PrettyTable
userInput = "" #Used for temporary user input throughout program
username = "" #Username of Current program user

menu = PrettyTable()
menu.field_names = ["Menu","Option"]
menu.add_rows([
        ["View Portfolio","V"],
        ["Add Stock","A"],
        ["Delete Stock","D"],
        ["Logout","L"]])


#Checks if the input matches one of the elements in params array
def check_input(input, params):
    for i in range(len(params)):
        if input == params[i]:
            return True
    return False

#Gets Input from user while checking for invalid inputs
def get_input(question, params): #if params = 0, it skips input checking
    userInput = input(question)
    if(params != 0):
        userInpuut = userInput.lower()
        while(check_input(userInput, params) != True):
            print("Invalid User Input, Try Again \n")
            userInput = input(question)
    return userInput

#Main Menu of Program (must pass login process)
def main_menu(current_user):
    menu_var = ""
    while(menu_var != "l"):
        menu_var = get_input(menu.get_string()+"\nEnter your Selection: ",["v","a","d","l"])
        if(menu_var == "v"):
            current_user.get_portfolio().print_portfolio()
        if(menu_var == "a"):
            current_user.get_portfolio().add_stock(
                get_input("Enter Stock Ticker: ",0),
                get_input("Enter Amount: ",0),
                get_input("Enter the Average Price: ",0))
        if(menu_var == "d"):
            current_user.get_portfolio().remove_stock(get_input("Enter Stock Ticker: ",0))
        if(menu_var == "l"):
            user.logout(current_user)

userInput = get_input("Do you want to login (L) or register (R)?: ", ["l","r"])

#Login
if(userInput == "l"):
  params = user.get_user_list()
  username = get_input("Enter your username: ", params)
  current_user = user.login(username)
  if(current_user.logged_in == True):
    print("Login Sucsessful!")
    main_menu(current_user)

#Register
if(userInput == "r"):
 username = get_input("Enter a new username: ", 0)
 if(user.register(username) == True):
     current_user = user.login(username)
     if(current_user.logged_in == True):
        print("Login Sucsessful!")
        main_menu(current_user)


print("Login/Registration Issue. Restart program") 