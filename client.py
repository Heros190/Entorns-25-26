import requests
class User:
    def __init__(self, username, nom, email, rol):
        self.username = username
        self.nom = nom
        self.email = email
        self.rol = rol
    
    def __str__(self):
        return self.nom
    

class daoUserClient:
    def getUserByUsername(self,username):
        # Petició HTTP al WebService (request)
        response = requests.get("http://localhost:5000/user?username="+username)
        # si la peticó ok code response = 200
        if response.status_code == 200:
            # obtenir dades JSON
            user_data_raw = response.json()
            # crear objecte User amb les dades JSON
            
            if 'msg' in user_data_raw.keys():
                return None
            # si no return None
            else: 
                user=User(user_data_raw['username'],user_data_raw['nom'],
                          user_data_raw['email'],
                          user_data_raw['rol'])
                return user
        return None
# Clase para mostrar la vista en consola
class ViewConsole:
    def getInputUsername(self):  # <-- self añadido
        username = input("Enter username: ")
        return username
    
    def showUserData(self, userData):  # <-- self añadido
        if userData is None:
            print("User not found")
        else:
            print("Username:", userData.username)
            print("Name:", userData.nom)
            print("Email:", userData.email)
            print("Role:", userData.rol)

# Supongo que tienes tu DAO y la clase User definidas
daoUserClient = daoUserClient()  # instancia de tu DAO

# Pedimos el username al usuario
view = ViewConsole()
username = view.getInputUsername()

# Buscamos al usuario en la "base de datos"
user = daoUserClient.getUserByUsername(username)

# Mostramos los datos
view.showUserData(user)
