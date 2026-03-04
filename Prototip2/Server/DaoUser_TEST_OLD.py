'''class UserDAO:
    def __init__(self, users_list):
        self.users = users_list  # referencia a la lista existente

    # 🔹 Obtener todos los usuarios
    def listAllUsers(self):
        return self.users

    # 🔹 Añadir usuario
    def addUser(self, user):
        # evitar ids duplicados
        if any(u.id == user.id for u in self.users):
            raise ValueError("User with this ID already exists")
        self.users.append(user)

    # 🔹 Actualizar usuario
    def updateUser(self, user):
        for i, u in enumerate(self.users):
            if u.id == user.id:
                self.users[i] = user
                return
        raise ValueError("User not found")

    # 🔹 Borrar usuario por id
    def deleteUser(self, user_id):
        for u in self.users:
            if u.id == user_id:
                self.users.remove(u)
                return
        raise ValueError("User not found")

    # 🔹 Buscar por email
    def searchByEmail(self, email):
        for u in self.users:
            if u.email == email:
                return u
        return None
'''
'''' 
    def login(self, identifier, password):
        for user in self.users:
            if (user.username == identifier or user.email == identifier) and user.password == password:
                return user
        return None
    
class ChildDAO:
    def __init__(self, children_list, relation_user_child):
        self.children = children_list  # referencia a la lista existente
        self.relation_user_child = relation_user_child  # referencia a la lista existente

    def getChilds(self, user): 
        # Get IDs from relations
        child_ids = {r['child_id'] 
                     for r in self.relation_user_child if r['user_id'] == user.id}
        # Return Child objects
        return [c for c in self.children if c.id in child_ids]
'''