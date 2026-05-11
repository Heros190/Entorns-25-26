from User import *
from DaoUserClient import *

class ViewConsole:

    

    def __init__(self):
        self.daoClient = DaoUserClient()
        self.token = ""
        self.selected_child_id = None   # 👈 AQUÍ
   
    def viewShowMenu(self):
        print("1: Login")
        print("2: Login Token")
        print("3: Child")
        print("4: Taps")
        print("5: Quit")
        while(True):
            option=input("Enter Option: ")
            if(option.isdigit()):
                optionInt=int(option)
                if(optionInt >0 and optionInt <6):
                    return optionInt
            
            print("Error: Introdueix una opció correcta")

        
    def viewGeneral(self):
        option=-1
        while(True):
            option=self.viewShowMenu()
            match option:
                case 1:
                    #login
                    self.viewLogin()
                case 2:
                    #login Token
                    self.viewLoginToken(self.token)
                case 3:
                    #Childs
                    print("View Childs")
                    self.viewChilds(self.token)
                    #self.viewLogin()
                case 4:
                    # Taps
                    print("View Taps")
                    self.viewTaps(self.token)
                case 5:
                    # Quit
                    exit()
                    print("Adeu, Gràcies per utilitzar l'aplicació")


    def viewChilds(self, token):
        print("View Childs")

        resposta_child = self.daoClient.childToken(token)

        if resposta_child:
            childs = resposta_child

            print("Children disponibles:")

            for c in childs:
                print(f"ID: {c['id']} | Name: {c['child_name']}")

            # ✔ SI SOLO HAY UNO, LO GUARDAS AUTOMÁTICAMENTE
            if len(childs) == 1:
                self.selected_child_id = childs[0]['id']
                print("Child seleccionado automáticamente:", self.selected_child_id)

            else:
                self.selected_child_id = input("Selecciona child_id: ")

        else:
            print("No children found")              
        
    def viewTaps(self, token):
        print("View Taps")

        if not token:
            print("ERROR: no login")
            return

        resposta_child = self.daoClient.childToken(token)

        if not resposta_child:
            print("ERROR: no children")
            return

        childs = resposta_child

        # CASO 1: ninguno
        if len(childs) == 0:
            print("No children available")
            return

        # CASO 2: uno solo
        if len(childs) == 1:
            self.selected_child_id = childs[0]['id']
            print("Auto-selected child:", self.selected_child_id)

        # CASO 3: varios
        else:
            print("Children disponibles:")
            for c in childs:
                print(f"{c['id']} - {c['child_name']}")

            self.selected_child_id = input("Selecciona child_id: ")

        # VALIDACIÓN FINAL
        if not str(self.selected_child_id).isdigit():
            print("ERROR: child_id inválido")
            return

        # LLAMADA TAPS
        resposta_taps = self.daoClient.tapToken(token, self.selected_child_id)

        if not resposta_taps:
            print("ERROR: backend no responde")
            return

        if resposta_taps.get('coderesponse') == '1':
            for tap in resposta_taps['data']:
                print(f"{tap['child_id']} | {tap['status_id']} | {tap['init']}")
        else:
            print("No taps found")
        
    def viewLoginToken(self, token):
        print("View LOGIN TOKEN")
        resposta_user=self.daoClient.loginToken(token)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()

    def viewLogin(self):
        print("View LOGIN")
        print("Introdueix el Username o email i el password")
        username=input("Username o email: ")
        passwd=input("Password: ")
        user=User("", username, passwd, "", "", "")
        resposta_user=self.daoClient.login(user)
        if(resposta_user):
            self.viewUser(resposta_user)
            self.token=resposta_user.token
        else:
            self.viewUserNotAutenticated()
    
    def viewUser(self,user):
        print("View User Authenticated")
        print(user)
    
    def viewUserNotAutenticated(self):
        print("View User")
        print("User NOT Authenticated")


viewConsole=ViewConsole()

viewConsole.viewGeneral()


