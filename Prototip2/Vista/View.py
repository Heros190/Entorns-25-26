class ViewConsole:

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
        password = input("Enter your password: ")
        return email, password
    
    
ViewConsole().viewGeneral()