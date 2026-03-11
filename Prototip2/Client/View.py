from User import *
from Child import *
from DaoUserClient import *
user
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
                    #break
                case 2:
                    #quit
                    print("Goodbye!")
                    break
                case _:
                    print("Invalid option. Please try again.")
    
    def viewLogin(self):
        username = ""
        email = input("Enter your username or email: ")
        if "@" not in email:
            username = email
            email = ""
        password = input("Enter your password: ")
        user=User("",username, password , email,"","") # username, email, password, idrole, token
        child=Child("","","","","") # id, child_name, sleep_average, treatment_id, time
        resposta=self.daoClient.login(user)
        if(resposta):
            self.viewUser(resposta)
            self.viewChilds(resposta)
        else:
            self.viewUserNotAuthenticated()
    
    def viewUser(self, user):
        print(f"Welcome, {user.username}!")
        # Here you can add more options for the authenticated user

    def viewUserNotAuthenticated(self):
        print("Authentication failed. Please check your credentials and try again.")
        self.viewGeneral()


    def viewChilds(self, user: User):
        childs = self.daoClient.getChilds(user)
        if not childs:
            print("No children found for this user.")
            return
        print("Your children:")
        for child in childs:
            print(f"- {child.child_name} (ID: {child.id}, Sleep avg: {child.sleep_average}h, Treatment ID: {child.treatment_id})")


# --- main function OUTSIDE the class ---
def main():
    view_console = ViewConsole()
    view_console.viewGeneral()


if __name__ == "__main__":
    main()