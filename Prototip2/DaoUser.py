class UserDAO:
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
