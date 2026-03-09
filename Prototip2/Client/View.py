from User import *;
from DaoUserClient import *;

class ViewConsole:

    def __init__(self):
        # Initialize your DAO client here
        self.daoClient = DaoUserClient()  # Make sure DaoUserClient exists

    def viewShowMenu(self):
        print("1: Login")
        print("2: Quit")
        while(True):
            opt = input ("Select an option: ")
            if (opt.isdigit()):
                if (int(opt) in [1, 2]):
                    return int(opt)
                else:
                    print("Invalid option. Please try again.")
            else:
                print("Invalid input. Please enter a number.")

    def viewGeneral(self):
        option = -1
        while (option != 2):
            option = self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                    break
                case 2:
                    #quit
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid option. Please try again.")
    
    def viewLogin(self):
        email = input("Enter your username or email: ")
        if "@" not in email:
            username = email
            email = ""
        password = input("Enter your password: ")
        user=User(username, email , password,"","") # username, email, password, idrole, token
        resposta=self.daoClient.login(user)
        if(resposta):
            self.viewUser(resposta)
        else:
            self.viewUserNotAuthenticated()
    
    def viewUser(self, user):
        print(f"Welcome, {user.name}!")
        # Here you can add more options for the authenticated user

    def viewUserNotAuthenticated(self):
        print("Authentication failed. Please check your credentials and try again.")
        self.viewGeneral()

# --- main function OUTSIDE the class ---
def main():
    view_console = ViewConsole()
    view_console.viewGeneral()


if __name__ == "__main__":
    main()