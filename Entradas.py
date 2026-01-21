# poo_entradas.py

from datetime import date

# -------------------------
# Clase base: Usuario
# -------------------------
class Usuario:
    def __init__(self, nom, email, contrasenya):
        self.nom = nom
        self.email = email
        self.contrasenya = contrasenya

    def registrar(self):
        print(f"{self.nom} se ha registrado con el email {self.email}.")

    def iniciar_sessio(self):
        print(f"{self.nom} ha iniciado sesión.")

# -------------------------
# Subclase: Cliente
# -------------------------
class Cliente(Usuario):
    def __init__(self, nom, email, contrasenya):
        super().__init__(nom, email, contrasenya)
        self.entradas_compradas = []

    def comprar_entrada(self, entrada):
        if entrada.estat == "Disponible":
            entrada.marcar_com_vendida()
            entrada.assignar_client(self)
            self.entradas_compradas.append(entrada)
            print(f"{self.nom} ha comprado la entrada para {entrada.esdeveniment.nom}.")
        else:
            print("La entrada no está disponible.")

    def veure_entrades(self):
        print(f"Entradas de {self.nom}:")
        for e in self.entradas_compradas:
            print(f"- {e.esdeveniment.nom}, {e.preu}€")

# -------------------------
# Subclase: Administrador
# -------------------------
class Administrador(Usuario):
    def __init__(self, nom, email, contrasenya):
        super().__init__(nom, email, contrasenya)
        self.esdeveniments = []

    def crear_esdeveniment(self, esdeveniment):
        self.esdeveniments.append(esdeveniment)
        esdeveniment.administrador = self
        print(f"{self.nom} ha creado el evento {esdeveniment.nom}.")

    def modificar_esdeveniment(self, esdeveniment, nou_nom=None):
        if nou_nom:
            print(f"Evento {esdeveniment.nom} modificado a {nou_nom}.")
            esdeveniment.nom = nou_nom

    def eliminar_esdeveniment(self, esdeveniment):
        if esdeveniment in self.esdeveniments:
            self.esdeveniments.remove(esdeveniment)
            print(f"{self.nom} ha eliminado el evento {esdeveniment.nom}.")

# -------------------------
# Clase: Esdeveniment
# -------------------------
class Esdeveniment:
    def __init__(self, nom, descripcio, data, ubicacio, entradesDisponibles):
        self.nom = nom
        self.descripcio = descripcio
        self.data = data
        self.ubicacio = ubicacio
        self.entradesDisponibles = entradesDisponibles
        self.administrador = None
        self.entrades = []

    def afegir_entrada(self, entrada):
        self.entrades.append(entrada)
        print(f"Entrada agregada al evento {self.nom}.")

    def mostrar_detalls(self):
        print(f"{self.nom} ({self.descripcio}) - {self.data} en {self.ubicacio}")
        print(f"Entradas disponibles: {self.entradesDisponibles}")

# -------------------------
# Clase: Entrada
# -------------------------
class Entrada:
    def __init__(self, esdeveniment, preu):
        self.esdeveniment = esdeveniment
        self.preu = preu
        self.estat = "Disponible"
        self.client = None

    def marcar_com_vendida(self):
        self.estat = "Venuda"

    def assignar_client(self, client):
        self.client = client

    def mostrar_info(self):
        estat = f"{self.estat}"
        if self.client:
            estat += f" - Comprada por {self.client.nom}"
        print(f"Entrada para {self.esdeveniment.nom}: {self.preu}€, {estat}")

# -------------------------
# Simulación básica
# -------------------------
# Crear administrador
admin1 = Administrador("Ana", "ana@empresa.com", "1234")
admin1.registrar()
admin1.iniciar_sessio()

# Crear eventos
evento1 = Esdeveniment("Concierto Rock", "Concierto de rock clásico", date(2026, 2, 15), "Auditorio Central", 5)
evento2 = Esdeveniment("Teatro Clásico", "Obra de Shakespeare", date(2026, 3, 5), "Teatro Principal", 3)

admin1.crear_esdeveniment(evento1)
admin1.crear_esdeveniment(evento2)

# Agregar entradas a eventos
for _ in range(evento1.entradesDisponibles):
    entrada = Entrada(evento1, 50.0)
    evento1.afegir_entrada(entrada)

for _ in range(evento2.entradesDisponibles):
    entrada = Entrada(evento2, 30.0)
    evento2.afegir_entrada(entrada)

# Crear clientes
cliente1 = Cliente("Luis", "luis@mail.com", "abcd")
cliente1.registrar()
cliente1.iniciar_sessio()

# Cliente compra entradas
cliente1.comprar_entrada(evento1.entrades[0])
cliente1.comprar_entrada(evento2.entrades[0])

# Mostrar entradas compradas
cliente1.veure_entrades()

# Mostrar información de entradas
print("\nEstado de todas las entradas del Concierto Rock:")
for e in evento1.entrades:
    e.mostrar_info()
